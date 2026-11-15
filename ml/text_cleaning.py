"""Single source of truth for turning a raw email into model input.

Training scripts AND the backend must import clean() from here, so the model sees
text cleaned in exactly the same way at training time and at prediction time.
"""
import re

MAX_CHARS = 3000


def clean(subject: str, body: str) -> str:
    subject = re.sub(r"^(\s*(re|fwd?)\s*:\s*)+", "", subject, flags=re.I)
    subject = re.sub(r"\[[^\]]{1,40}\]", " ", subject)         # list tags like [Python-Dev]
    body = re.sub(r"(?m)^\s*>.*$", " ", body)                   # quoted reply lines
    text = f"{subject}\n{body}"
    text = re.sub(r"<[^>]+>", " ", text)                        # leftover HTML tags
    text = re.sub(r"=\?[\w-]+\?[bBqQ]\?[^?]*\?=", " ", text)    # undecoded encoded-words
    text = re.sub(r"https?://\S+|www\.\S+", " [URL] ", text)
    text = re.sub(r"\S+@\S+\.\S+", " [EMAIL] ", text)
    return re.sub(r"\s+", " ", text).strip()[:MAX_CHARS]


def dedupe_key(text: str) -> str:
    """Used only when building the dataset (not at prediction time)."""
    return re.sub(r"\d+", "0", text.lower())[:400]
