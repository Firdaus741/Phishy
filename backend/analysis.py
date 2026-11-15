"""The full per-email analysis, shared by the /predict endpoint and scan_inbox.py.

Keep it in one place so the API and the command-line scan can never drift apart.
"""
import os
from email.utils import parseaddr

from classifier import PhishingClassifier
from header_checks import check_headers
from link_checks import VirusTotal, check_links

# Placeholder cutoff for the text model alone. The final Safe/Phishing verdict will combine
# text, header and link signals; this value is only what is reported for the text part.
TEXT_THRESHOLD = float(os.environ.get("PHISHY_TEXT_THRESHOLD", "0.5"))


def analyze(clf: PhishingClassifier, vt: VirusTotal | None, *, subject: str = "", body: str = "",
            html: str = "", sender: str = "", reply_to: str = "",
            authentication_results: str = "") -> dict | None:
    """Text probability + header result + link result. Returns None if there is no usable text."""
    prob, text = clf.score_email(subject, body, html)
    if not text:
        return None
    headers = check_headers({"from": sender, "reply_to": reply_to,
                             "authentication_results": authentication_results})
    addr = parseaddr(sender)[1]
    sender_domain = addr.rsplit("@", 1)[-1] if "@" in addr else ""
    links = check_links(body, html, vt, sender_domain)
    return {
        "phishing_probability": round(prob, 4),
        "text_label": "phishing" if prob >= TEXT_THRESHOLD else "safe",
        "threshold": TEXT_THRESHOLD,
        "model": clf.name,
        "headers": headers,
        "links": links,
    }
