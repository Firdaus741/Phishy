"""Link checks: pull the URLs out of an email, apply local rules, look them up on VirusTotal.

Design rules
- We NEVER open or fetch the links ourselves. VirusTotal is asked about a URL by its id (a hash-like
  encoding), so nothing from the email is visited.
- VirusTotal is a lookup only: unknown URLs are NOT submitted for scanning (that would share them).
- Privacy: by default only scheme + host + path are sent, never the query string or fragment,
  because those often carry the recipient's address or a login token. Trade-off: fewer exact matches.
  Set VT_STRIP_QUERY=false to send the full URL.
- The free tier allows about 4 requests per minute: results are cached (sqlite, 24 h), at most
  MAX_URLS links are checked per email, and when the limit is hit a link is reported as "unchecked"
  instead of making the request wait. The API key is read from backend/.env (VT_API_KEY).
- A VirusTotal failure never breaks a prediction: the link is reported as "unchecked" with a reason.
"""
import base64
import ipaddress
import json
import os
import re
import sqlite3
import threading
import time
from collections import deque
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import httpx
from dotenv import load_dotenv

from header_checks import registered_domain

load_dotenv(Path(__file__).parent / ".env")

VT_API = "https://www.virustotal.com/api/v3/urls/"
MAX_URLS = int(os.environ.get("VT_MAX_URLS", "3"))  # links looked up per email (free tier: 4 requests/minute)
DAILY_CAP = int(os.environ.get("VT_DAILY_CAP", "450"))  # stay under the free daily quota (500), survives restarts
BACKOFF_SECONDS = 60         # after VirusTotal says "too many requests", stop calling it for this long
VT_MALICIOUS_MIN = 2         # engines needed to call a link "malicious" (1 engine = "suspicious": VT has false positives)
CACHE_PATH = Path(os.environ.get("PHISHY_VT_CACHE", Path(__file__).parent / "vt_cache.sqlite"))
CACHE_TTL = 24 * 3600        # known results
UNKNOWN_TTL = 3600           # "VirusTotal has never seen it": check again sooner

SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd", "buff.ly", "cutt.ly",
              "rebrand.ly", "shorturl.at"}
STRONG_FLAGS = {"ip_host", "punycode", "userinfo", "text_mismatch"}  # shorteners alone are common in real mail

URL_RE = re.compile(r"https?://[^\s<>\"'\)\]]+", re.I)
ANCHOR_RE = re.compile(r"(?is)<a\b[^>]*?href\s*=\s*[\"']?([^\"'\s>]+)[^>]*>(.*?)</a>")
VISIBLE_DOMAIN_RE = re.compile(r"(?i)\b(?:https?://)?((?:[a-z0-9-]+\.)+[a-z]{2,})\b")


# ----------------------------------------------------------------------------- extraction + local rules
def _normalise(url: str) -> str | None:
    url = url.strip().rstrip(".,;:!?)")
    try:
        parts = urlsplit(url)
    except ValueError:
        return None
    if parts.scheme.lower() not in ("http", "https") or not parts.hostname:
        return None
    netloc = parts.netloc.lower()
    return urlunsplit((parts.scheme.lower(), netloc, parts.path, parts.query, ""))  # drop #fragment


def _host(url: str) -> str:
    return (urlsplit(url).hostname or "").lower()


def extract_links(body_text: str = "", body_html: str = "") -> dict[str, list[str]]:
    """Returns {url: [text_mismatch description, ...]} for every distinct link found."""
    found: dict[str, list[str]] = {}
    for href, inner in ANCHOR_RE.findall(body_html or ""):
        url = _normalise(href)
        if not url:
            continue
        found.setdefault(url, [])
        visible = re.sub(r"<[^>]+>", " ", inner)
        m = VISIBLE_DOMAIN_RE.search(visible)
        if m and registered_domain(m.group(1)) != registered_domain(_host(url)):
            found[url].append(f"link text shows {m.group(1).lower()} but goes to {_host(url)}")
    for raw in URL_RE.findall(f"{body_text or ''}\n{body_html or ''}"):
        url = _normalise(raw)
        if url:
            found.setdefault(url, [])
    return found


def local_flags(url: str, mismatches: list[str]) -> list[str]:
    host = _host(url)
    flags = []
    try:
        ipaddress.ip_address(host)
        flags.append("ip_host")
    except ValueError:
        pass
    if any(label.startswith("xn--") for label in host.split(".")):
        flags.append("punycode")
    if urlsplit(url).username is not None:
        flags.append("userinfo")
    if registered_domain(host) in SHORTENERS:
        flags.append("shortener")
    if mismatches:
        flags.append("text_mismatch")
    return flags


# ----------------------------------------------------------------------------- VirusTotal
def _vt_id(url: str) -> str:
    return base64.urlsafe_b64encode(url.encode()).decode().rstrip("=")


def _status(stats: dict) -> str:
    m, s = stats.get("malicious", 0), stats.get("suspicious", 0)
    if m >= VT_MALICIOUS_MIN:
        return "malicious"
    if m >= 1 or s >= 1:
        return "suspicious"
    return "clean" if (stats.get("harmless", 0) + stats.get("undetected", 0)) > 0 else "unknown"


class VirusTotal:
    def __init__(self, api_key: str | None = None, http: httpx.Client | None = None,
                 cache_path: Path = CACHE_PATH, per_minute: int = 4, clock=time.time,
                 strip_query: bool | None = None, daily_cap: int = DAILY_CAP):
        self.api_key = api_key if api_key is not None else os.environ.get("VT_API_KEY", "")
        self.http = http or httpx.Client(timeout=5.0)
        self.cache_path = Path(cache_path)
        self.per_minute = per_minute
        self.clock = clock
        self.strip_query = (os.environ.get("VT_STRIP_QUERY", "true").lower() != "false"
                            if strip_query is None else strip_query)
        self.daily_cap = daily_cap
        self._sent: deque[float] = deque()
        self._blocked_until = 0.0
        self._lock = threading.Lock()
        with sqlite3.connect(self.cache_path) as db:
            db.execute("CREATE TABLE IF NOT EXISTS cache (url TEXT PRIMARY KEY, ts REAL, result TEXT)")
            db.execute("CREATE TABLE IF NOT EXISTS usage (day TEXT PRIMARY KEY, n INTEGER)")

    def _today(self) -> str:
        return time.strftime("%Y-%m-%d", time.gmtime(self.clock()))  # VirusTotal's day is UTC

    def requests_today(self) -> int:
        with sqlite3.connect(self.cache_path) as db:
            row = db.execute("SELECT n FROM usage WHERE day = ?", (self._today(),)).fetchone()
        return row[0] if row else 0

    def _count_request(self) -> None:
        with sqlite3.connect(self.cache_path) as db:
            db.execute("INSERT INTO usage VALUES (?, 1) ON CONFLICT(day) DO UPDATE SET n = n + 1", (self._today(),))

    @property
    def enabled(self) -> bool:
        return bool(self.api_key)

    def _cached(self, url: str):
        with sqlite3.connect(self.cache_path) as db:
            row = db.execute("SELECT ts, result FROM cache WHERE url = ?", (url,)).fetchone()
        if not row:
            return None
        result = json.loads(row[1])
        ttl = UNKNOWN_TTL if result["status"] == "unknown" else CACHE_TTL
        return result if self.clock() - row[0] < ttl else None

    def _store(self, url: str, result: dict) -> None:
        with sqlite3.connect(self.cache_path) as db:
            db.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?)", (url, self.clock(), json.dumps(result)))

    def _allow_request(self) -> bool:
        with self._lock:
            now = self.clock()
            while self._sent and now - self._sent[0] >= 60:
                self._sent.popleft()
            if len(self._sent) >= self.per_minute:
                return False
            self._sent.append(now)
            return True

    def lookup(self, url: str) -> dict:
        if not self.enabled:
            return {"status": "unchecked", "reason": "no_api_key"}
        sent = url
        if self.strip_query:
            p = urlsplit(url)
            sent = urlunsplit((p.scheme, p.netloc, p.path, "", ""))
        cached = self._cached(sent)
        if cached:
            return {**cached, "cached": True}
        if self.clock() < self._blocked_until:
            return {"status": "unchecked", "reason": "backing_off"}
        if self.requests_today() >= self.daily_cap:
            return {"status": "unchecked", "reason": "daily_cap"}
        if not self._allow_request():
            return {"status": "unchecked", "reason": "rate_limited"}
        self._count_request()  # count every real request, even a failed one: be conservative
        try:
            r = self.http.get(VT_API + _vt_id(sent), headers={"x-apikey": self.api_key})
        except httpx.HTTPError:
            return {"status": "unchecked", "reason": "error"}
        if r.status_code == 200:
            stats = r.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            result = {"status": _status(stats), "malicious": stats.get("malicious", 0),
                      "suspicious": stats.get("suspicious", 0)}
        elif r.status_code == 404:
            result = {"status": "unknown", "malicious": 0, "suspicious": 0}
        elif r.status_code in (401, 403):
            return {"status": "unchecked", "reason": "invalid_api_key"}
        elif r.status_code == 429:
            self._blocked_until = self.clock() + BACKOFF_SECONDS  # stop hammering a limit we already hit
            return {"status": "unchecked", "reason": "quota_exceeded"}
        else:
            return {"status": "unchecked", "reason": "error"}
        self._store(sent, result)
        return result


# ----------------------------------------------------------------------------- the check used by /predict
def check_links(body_text: str = "", body_html: str = "", vt: VirusTotal | None = None,
                sender_domain: str = "") -> dict:
    found = extract_links(body_text, body_html)
    items = [{"url": u, "host": _host(u), "flags": local_flags(u, mm), "mismatch": mm} for u, mm in found.items()]
    sender = registered_domain(sender_domain) if sender_domain else ""

    # The per-email cap and the 4/minute limit mean we must choose which links to look up:
    # 1) links with a strong local flag, 2) links to a different domain than the sender's, 3) the rest.
    def priority(i):
        if set(i["flags"]) & STRONG_FLAGS:
            return 0
        return 2 if sender and registered_domain(i["host"]) == sender else 1

    items.sort(key=priority)  # stable: keeps the original order inside each group
    reasons = []
    for n, item in enumerate(items):
        if vt is not None and n < MAX_URLS:
            item["virustotal"] = vt.lookup(item["url"])
        else:
            item["virustotal"] = {"status": "unchecked", "reason": "not_looked_up" if vt else "no_api_key"}
        status = item["virustotal"]["status"]
        if status in ("malicious", "suspicious"):
            reasons.append(f"VirusTotal marks {item['host']} {status} "
                           f"({item['virustotal']['malicious']} engines)")
        for flag in item["flags"]:
            if flag in STRONG_FLAGS:
                reasons.append(f"{item['host']}: {flag}")
        reasons.extend(item["mismatch"])
        del item["mismatch"]
    suspicious = any(i["virustotal"]["status"] == "malicious" or set(i["flags"]) & STRONG_FLAGS for i in items)
    return {
        "total_found": len(items),
        "looked_up": sum(1 for i in items if i["virustotal"]["status"] != "unchecked"),
        "vt_enabled": bool(vt and vt.enabled),
        "suspicious": suspicious,
        "reasons": list(dict.fromkeys(reasons)),
        "urls": items[:20],  # never return an unbounded list
    }
