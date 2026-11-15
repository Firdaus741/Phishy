"""Rule-based email header checks (no training: the datasets have no usable headers).

Input: a parsed email dict from gmail_client.parse_message().
Output: the raw SPF/DKIM/DMARC results plus a few simple, explainable flags.

Trust rule: SPF/DKIM/DMARC are only believed when the topmost Authentication-Results header
was added by Gmail's own server (authserv-id ends in google.com). A sender can forge that
header, so a result from any other server is reported as "unverified" and ignored.

  suspicious = auth_failed OR display_name_brand_mismatch      (strong signals)
  reply_to_mismatch is reported but is a weak signal (mailing platforms do this legitimately).
"""
import re
from email.utils import parseaddr

SPF_FAIL = {"fail", "softfail"}
DKIM_FAIL = {"fail"}
DMARC_FAIL = {"fail"}

# Registered domains that may legitimately use a brand name in the display name.
# Illustrative and short on purpose: verify and extend before relying on it, and state it as a limitation.
BRAND_DOMAINS = {
    "paypal": {"paypal.com"},
    "google": {"google.com", "gmail.com", "youtube.com"},
    "microsoft": {"microsoft.com", "outlook.com", "live.com", "office.com", "microsoftonline.com"},
    "apple": {"apple.com", "icloud.com"},
    "amazon": {"amazon.com", "amazon.co.uk"},
    "facebook": {"facebook.com", "facebookmail.com", "meta.com"},
    "netflix": {"netflix.com"},
    "dhl": {"dhl.com"},
    "maybank": {"maybank.com", "maybank2u.com.my", "maybank.com.my"},
    "cimb": {"cimb.com", "cimbclicks.com.my", "cimb.com.my"},
    "public bank": {"publicbank.com.my"},
    "rhb": {"rhbgroup.com", "rhbbank.com.my"},
    "bank islam": {"bankislam.com.my", "bankislam.com"},
    "lhdn": {"hasil.gov.my"},
    "pos malaysia": {"pos.com.my"},
}
TWO_PART_SUFFIXES = {"com.my", "gov.my", "edu.my", "org.my", "net.my", "co.uk", "org.uk", "com.au"}


def _address_domain(value: str) -> str:
    addr = parseaddr(value or "")[1]
    return addr.rsplit("@", 1)[-1].lower().strip() if "@" in addr else ""


def registered_domain(domain: str) -> str:
    """Rough 'example.com' / 'example.com.my' from a host name (no external list needed)."""
    labels = [x for x in domain.lower().split(".") if x]
    if len(labels) >= 3 and ".".join(labels[-2:]) in TWO_PART_SUFFIXES:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


def _result(auth: str, method: str) -> str:
    """Overall result for spf/dkim/dmarc. DKIM can appear several times: any pass wins."""
    values = [v.lower() for v in re.findall(rf"\b{method}=(\w+)", auth, flags=re.I)]
    if not values:
        return "none"
    return "pass" if "pass" in values else values[0]


def check_headers(email: dict) -> dict:
    auth = email.get("authentication_results", "") or ""
    authserv = auth.split(";", 1)[0].strip().lower()
    verified = authserv == "google.com" or authserv.endswith(".google.com")

    spf, dkim, dmarc = (_result(auth, m) for m in ("spf", "dkim", "dmarc"))
    reasons = []

    auth_failed = False
    if verified:
        for name, value, bad in (("SPF", spf, SPF_FAIL), ("DKIM", dkim, DKIM_FAIL), ("DMARC", dmarc, DMARC_FAIL)):
            if value in bad:
                auth_failed = True
                reasons.append(f"{name} {value}")
    elif auth:
        reasons.append(f"authentication results not from Gmail ({authserv or 'unknown'}): ignored")

    display_name, from_addr = parseaddr(email.get("from", "") or "")
    from_domain = _address_domain(email.get("from", ""))
    from_reg = registered_domain(from_domain) if from_domain else ""

    reply_domain = _address_domain(email.get("reply_to", ""))
    reply_to_mismatch = bool(reply_domain and from_reg and registered_domain(reply_domain) != from_reg)
    if reply_to_mismatch:
        reasons.append(f"Reply-To domain ({reply_domain}) differs from sender ({from_domain})")

    brand_hit = None
    name = display_name.lower()
    for brand, domains in BRAND_DOMAINS.items():
        if re.search(rf"\b{re.escape(brand)}\b", name) and from_reg not in domains:
            brand_hit = brand
            reasons.append(f'display name mentions "{brand}" but the sender domain is {from_domain or "missing"}')
            break

    return {
        "auth_verified": verified,
        "spf": spf,
        "dkim": dkim,
        "dmarc": dmarc,
        "auth_failed": auth_failed,
        "reply_to_mismatch": reply_to_mismatch,
        "display_name_brand_mismatch": brand_hit,
        "suspicious": auth_failed or brand_hit is not None,
        "reasons": reasons,
    }


if __name__ == "__main__":
    # Live check on your own inbox (opens the Google login if token.json is missing or expired).
    from gmail_client import fetch_recent_emails

    for e in fetch_recent_emails(10):
        r = check_headers(e)
        flag = "SUSPICIOUS" if r["suspicious"] else "ok"
        print(f"[{flag:10s}] {e['from'][:45]:45s} spf={r['spf']} dkim={r['dkim']} dmarc={r['dmarc']} verified={r['auth_verified']}")
        for reason in r["reasons"]:
            print("             -", reason)
