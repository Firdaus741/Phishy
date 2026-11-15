"""Gmail access for Phishy: OAuth2 login, fetching and parsing emails."""
import base64
from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
BASE_DIR = Path(__file__).parent  # the backend folder, wherever you run from
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"


def get_credentials() -> Credentials:
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds and not creds.valid:
        if creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                creds = None  # expired or revoked: log in again
        else:
            creds = None
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        creds = flow.run_local_server(port=0)
    TOKEN_FILE.write_text(creds.to_json())
    return creds


def get_service():
    return build("gmail", "v1", credentials=get_credentials())


def _decode(data: str) -> str:
    padded = data + "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(padded).decode("utf-8", errors="replace")


def _extract_bodies(payload: dict) -> tuple[str, str]:
    """Walk the MIME tree and return (plain_text, html)."""
    plain, html = "", ""
    mime = payload.get("mimeType", "")
    data = payload.get("body", {}).get("data")
    if data and mime == "text/plain":
        plain = _decode(data)
    elif data and mime == "text/html":
        html = _decode(data)
    for part in payload.get("parts", []) or []:
        p, h = _extract_bodies(part)
        plain += p
        html += h
    return plain, html


def parse_message(msg: dict) -> dict:
    payload = msg["payload"]
    headers = {}
    for h in payload.get("headers", []):
        headers.setdefault(h["name"].lower(), h["value"])  # keep the topmost copy
    plain, html = _extract_bodies(payload)
    return {
        "id": msg["id"],
        "from": headers.get("from", ""),
        "reply_to": headers.get("reply-to", ""),
        "return_path": headers.get("return-path", ""),
        "subject": headers.get("subject", ""),
        "date": headers.get("date", ""),
        "authentication_results": headers.get("authentication-results", ""),
        "received_spf": headers.get("received-spf", ""),
        "body_text": plain,
        "body_html": html,
    }


def fetch_recent_emails(max_results: int = 5, label: str = "INBOX") -> list[dict]:
    """Newest emails in a Gmail label, e.g. "INBOX" or "SPAM" (read-only)."""
    service = get_service()
    resp = (
        service.users()
        .messages()
        .list(userId="me", maxResults=max_results, labelIds=[label])
        .execute()
    )
    emails = []
    for ref in resp.get("messages", []):
        msg = (
            service.users().messages().get(userId="me", id=ref["id"], format="full").execute()
        )
        emails.append(parse_message(msg))
    return emails


if __name__ == "__main__":
    for e in fetch_recent_emails(5):
        print("-", e["subject"][:70], "|", e["from"][:40])
        print("   auth:", e["authentication_results"][:90])