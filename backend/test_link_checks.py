"""Tests for link_checks.py with a FAKE VirusTotal (no real network calls, no API key needed).
Run: python backend\\test_link_checks.py
"""
import tempfile
from pathlib import Path

import httpx

import link_checks as lc
from link_checks import VirusTotal, check_links, extract_links, local_flags


class Clock:
    def __init__(self):
        self.t = 1_000_000.0

    def __call__(self):
        return self.t


def make_vt(handler, key="test-key", cache=None, **kw):
    transport = httpx.MockTransport(handler)
    cache = cache or Path(tempfile.mkdtemp()) / "cache.sqlite"
    return VirusTotal(api_key=key, http=httpx.Client(transport=transport), cache_path=cache, **kw)


def vt_reply(malicious=0, suspicious=0, harmless=60):
    stats = {"malicious": malicious, "suspicious": suspicious, "harmless": harmless, "undetected": 5}
    return httpx.Response(200, json={"data": {"attributes": {"last_analysis_stats": stats}}})


# ---------------------------------------------------------------- extraction and local rules
def test_extract_plain_text_and_html():
    links = extract_links("see http://a.com/x, and https://b.org/y#frag.", '<a href="http://c.net/z">go</a>')
    assert set(links) == {"http://a.com/x", "https://b.org/y", "http://c.net/z"}  # punctuation + fragment dropped


def test_text_mismatch_is_detected():
    links = extract_links("", '<a href="http://evil.com/login">www.paypal.com</a>')
    assert links["http://evil.com/login"] and "paypal.com" in links["http://evil.com/login"][0]


def test_matching_link_text_is_fine():
    assert extract_links("", '<a href="https://www.paypal.com/x">paypal.com</a>')["https://www.paypal.com/x"] == []
    assert extract_links("", '<a href="http://evil.com/x">Click here</a>')["http://evil.com/x"] == []


def test_local_flags():
    assert "ip_host" in local_flags("http://192.168.1.5/login", [])
    assert "punycode" in local_flags("http://xn--pypal-4ve.com/", [])
    assert "userinfo" in local_flags("http://paypal.com@evil.com/", [])
    assert local_flags("http://bit.ly/abc", []) == ["shortener"]
    assert local_flags("https://example.com/", []) == []


# ---------------------------------------------------------------- VirusTotal client
def test_request_uses_url_id_and_key():
    seen = {}

    def handler(request):
        seen["path"], seen["key"] = request.url.path, request.headers["x-apikey"]
        return vt_reply()

    make_vt(handler).lookup("http://example.com/")
    assert seen == {"path": "/api/v3/urls/aHR0cDovL2V4YW1wbGUuY29tLw", "key": "test-key"}


def test_query_string_is_not_sent_by_default():
    paths = []
    vt = make_vt(lambda r: (paths.append(r.url.path), vt_reply())[1])
    vt.lookup("http://example.com/a?email=me@x.com&token=SECRET")
    assert paths == ["/api/v3/urls/" + lc._vt_id("http://example.com/a")]


def test_full_url_sent_when_strip_disabled():
    paths = []
    vt = make_vt(lambda r: (paths.append(r.url.path), vt_reply())[1], strip_query=False)
    vt.lookup("http://example.com/a?x=1")
    assert paths == ["/api/v3/urls/" + lc._vt_id("http://example.com/a?x=1")]


def test_status_mapping():
    assert make_vt(lambda r: vt_reply(malicious=5)).lookup("http://a.com/")["status"] == "malicious"
    assert make_vt(lambda r: vt_reply(malicious=1)).lookup("http://a.com/")["status"] == "suspicious"
    assert make_vt(lambda r: vt_reply(suspicious=2)).lookup("http://a.com/")["status"] == "suspicious"
    assert make_vt(lambda r: vt_reply()).lookup("http://a.com/")["status"] == "clean"


def test_unknown_url_is_not_submitted_and_is_cached():
    calls = []
    vt = make_vt(lambda r: (calls.append(r.method), httpx.Response(404))[1])
    assert vt.lookup("http://new.example/")["status"] == "unknown"
    again = vt.lookup("http://new.example/")
    assert again["status"] == "unknown" and again["cached"] and calls == ["GET"]  # only a lookup, once


def test_cache_prevents_second_request():
    calls = []
    vt = make_vt(lambda r: (calls.append(1), vt_reply(malicious=3))[1])
    vt.lookup("http://a.com/")
    assert vt.lookup("http://a.com/?x=1")["status"] == "malicious"  # same URL once the query is stripped
    assert len(calls) == 1


def test_cache_expires():
    clock, calls = Clock(), []
    vt = make_vt(lambda r: (calls.append(1), vt_reply())[1], clock=clock)
    vt.lookup("http://a.com/")
    clock.t += 25 * 3600
    vt.lookup("http://a.com/")
    assert len(calls) == 2


def test_rate_limit_does_not_wait_or_call():
    clock, calls = Clock(), []
    vt = make_vt(lambda r: (calls.append(1), vt_reply())[1], per_minute=2, clock=clock)
    vt.lookup("http://a.com/")
    vt.lookup("http://b.com/")
    third = vt.lookup("http://c.com/")
    assert third == {"status": "unchecked", "reason": "rate_limited"} and len(calls) == 2
    clock.t += 61
    assert vt.lookup("http://c.com/")["status"] == "clean"


def test_429_backs_off_then_resumes():
    clock, calls = Clock(), []
    answers = iter([httpx.Response(429), vt_reply()])
    vt = make_vt(lambda r: (calls.append(1), next(answers))[1], per_minute=100, clock=clock)
    assert vt.lookup("http://a.com/")["reason"] == "quota_exceeded"
    assert vt.lookup("http://b.com/")["reason"] == "backing_off" and len(calls) == 1  # no hammering
    clock.t += 61
    assert vt.lookup("http://b.com/")["status"] == "clean" and len(calls) == 2


def test_daily_cap_survives_restart():
    clock, cache = Clock(), Path(tempfile.mkdtemp()) / "shared.sqlite"
    first = make_vt(lambda r: vt_reply(), cache=cache, per_minute=100, clock=clock, daily_cap=2)
    first.lookup("http://a.com/")
    first.lookup("http://b.com/")
    restarted = make_vt(lambda r: vt_reply(), cache=cache, per_minute=100, clock=clock, daily_cap=2)
    assert restarted.requests_today() == 2
    assert restarted.lookup("http://c.com/") == {"status": "unchecked", "reason": "daily_cap"}
    clock.t += 24 * 3600  # next UTC day
    assert restarted.lookup("http://c.com/")["status"] == "clean"


def test_cache_hits_do_not_use_quota():
    vt = make_vt(lambda r: vt_reply())
    vt.lookup("http://a.com/")
    vt.lookup("http://a.com/")
    vt.lookup("http://a.com/")
    assert vt.requests_today() == 1


def test_other_domains_are_looked_up_before_the_senders_own():
    asked = []
    vt = make_vt(lambda r: (asked.append(r.url.path), vt_reply())[1], per_minute=100)
    text = "http://mybank.com/a http://mybank.com/b http://other.example/x"
    check_links(text, "", vt, sender_domain="mybank.com")
    assert asked[0] == "/api/v3/urls/" + lc._vt_id("http://other.example/x")  # unusual one goes first


def test_no_key_makes_no_request():
    calls = []
    vt = make_vt(lambda r: (calls.append(1), vt_reply())[1], key="")
    assert vt.lookup("http://a.com/") == {"status": "unchecked", "reason": "no_api_key"} and not calls


def test_errors_never_raise():
    assert make_vt(lambda r: httpx.Response(401)).lookup("http://a.com/")["reason"] == "invalid_api_key"
    assert make_vt(lambda r: httpx.Response(429)).lookup("http://a.com/")["reason"] == "quota_exceeded"
    assert make_vt(lambda r: httpx.Response(500)).lookup("http://a.com/")["reason"] == "error"

    def boom(request):
        raise httpx.ConnectError("no network")

    assert make_vt(boom).lookup("http://a.com/")["reason"] == "error"


# ---------------------------------------------------------------- check_links
def test_cap_and_strong_links_are_checked_first():
    asked = []
    vt = make_vt(lambda r: (asked.append(r.url.path), vt_reply())[1], per_minute=100)
    text = " ".join(f"http://site{i}.com/" for i in range(8)) + " http://10.0.0.9/login"
    out = check_links(text, "", vt)
    assert out["total_found"] == 9 and len(asked) == lc.MAX_URLS
    assert "/api/v3/urls/" + lc._vt_id("http://10.0.0.9/login") in asked  # the IP link made the cut
    assert out["suspicious"] and any("ip_host" in r for r in out["reasons"])


def test_clean_links_are_not_suspicious():
    out = check_links("read https://example.com/news", "", make_vt(lambda r: vt_reply()))
    assert out["total_found"] == 1 and not out["suspicious"] and out["looked_up"] == 1


def test_malicious_link_makes_email_suspicious():
    out = check_links("go to http://bad.example/x", "", make_vt(lambda r: vt_reply(malicious=8)))
    assert out["suspicious"] and "VirusTotal marks bad.example malicious" in out["reasons"][0]


def test_works_without_virustotal():
    out = check_links("", '<a href="http://evil.com/a">www.paypal.com</a>', None)
    assert out["suspicious"] and not out["vt_enabled"] and out["looked_up"] == 0


def test_no_links():
    assert check_links("hello there", "", None) == {"total_found": 0, "looked_up": 0, "vt_enabled": False,
                                                    "suspicious": False, "reasons": [], "urls": []}


if __name__ == "__main__":
    import traceback

    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    failed = 0
    for n, f in tests:
        try:
            f()
            print("ok  ", n)
        except Exception:
            failed += 1
            print("FAIL", n)
            traceback.print_exc()
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
