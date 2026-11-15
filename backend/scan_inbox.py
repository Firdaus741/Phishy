"""Run the full analysis (text model + headers + links) on your own Gmail. Read-only.

  python backend\\scan_inbox.py                    # newest 10 inbox emails
  python backend\\scan_inbox.py --count 20
  python backend\\scan_inbox.py --label SPAM       # your Spam folder: the best place to find real failures
  python backend\\scan_inbox.py --vt               # also look links up on VirusTotal (uses your quota)

Nothing is sent anywhere except, with --vt, the host + path of up to 3 links per email to VirusTotal.
VirusTotal is OFF by default because the free key allows only 4 lookups a minute, so a bulk scan
would use it up. Output stays on this screen; nothing is saved.
"""
import argparse
import sys

from analysis import analyze
from classifier import PhishingClassifier
from gmail_client import fetch_recent_emails
from link_checks import VirusTotal


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # subjects can contain any characters
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--label", default="INBOX", help="Gmail label: INBOX, SPAM, ...")
    ap.add_argument("--vt", action="store_true", help="look links up on VirusTotal")
    args = ap.parse_args()

    vt = VirusTotal() if args.vt else VirusTotal(api_key="")
    if args.vt and not vt.enabled:
        print("--vt given but no VT_API_KEY found in backend\\.env: links will be shown as unchecked.\n")

    print(f"Fetching {args.count} emails from {args.label} ...")
    emails = fetch_recent_emails(args.count, args.label)
    clf = PhishingClassifier()
    print(f"Model: {clf.name} | VirusTotal: {'on' if vt.enabled else 'off'}\n")

    flagged = 0
    for e in emails:
        r = analyze(clf, vt, subject=e["subject"], body=e["body_text"], html=e["body_html"], sender=e["from"],
                    reply_to=e["reply_to"], authentication_results=e["authentication_results"])
        who = f"{e['from'][:32]:32s} | {e['subject'][:45]}"
        if r is None:
            print(f"  (no text)  {who}")
            continue
        t, h, k = r["text_label"] == "phishing", r["headers"]["suspicious"], r["links"]["suspicious"]
        flagged += t or h or k
        print(f"p={r['phishing_probability']:.3f} text={'PHISH' if t else 'safe '} "
              f"hdr={'FLAG' if h else 'ok  '} link={'FLAG' if k else 'ok  '}  {who}")
        for reason in r["headers"]["reasons"] + r["links"]["reasons"]:
            print(f"             - {reason}")

    print(f"\n{len(emails)} emails scanned, {flagged} with at least one signal raised.")
    print("These are three separate signals, not the final verdict (the decision rule is not built yet).")


if __name__ == "__main__":
    main()
