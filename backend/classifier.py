"""Loads the fine-tuned DistilBERT once and scores emails (phishing probability 0..1).

Text is prepared with the SAME clean() used to build the training data (ml/text_cleaning.py).
Never copy that function here: a mismatch between training and prediction quietly hurts accuracy.
"""
import html as html_lib
import os
import re
import sys
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))
from text_cleaning import clean  # noqa: E402

MODEL_DIR = Path(os.environ.get("PHISHY_MODEL_DIR", ROOT / "backend" / "models" / "distilbert-base-uncased"))
MAX_LEN = 256  # must match ml/train.py
PHISHING_ID = 1  # labels: 0 = legit, 1 = phishing


def html_to_text(raw_html: str) -> str:
    """Plain text from an HTML-only email. Link targets are kept as visible URLs, because the
    training emails mostly show links as text and clean() turns them into [URL]."""
    t = re.sub(r"(?is)<(script|style|head)\b[^>]*>.*?</\1>", " ", raw_html)
    t = re.sub(r"(?is)<a\b[^>]*?href=[\"']?(https?://[^\"'\s>]+)[^>]*>", r" \1 ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</li>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return html_lib.unescape(t)


def email_text(subject: str, body_text: str = "", body_html: str = "") -> str:
    """Cleaned model input. Prefers the plain-text part; falls back to the HTML part."""
    body = body_text if body_text.strip() else html_to_text(body_html or "")
    return clean(subject or "", body or "")


class PhishingClassifier:
    def __init__(self, model_dir: Path = MODEL_DIR):
        self.name = Path(model_dir).name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir).to(self.device).eval()

    @torch.inference_mode()
    def predict_cleaned(self, texts: list[str], batch_size: int = 32) -> list[float]:
        """Phishing probability for texts that are ALREADY cleaned."""
        out: list[float] = []
        for i in range(0, len(texts), batch_size):
            enc = self.tokenizer(texts[i:i + batch_size], truncation=True, max_length=MAX_LEN,
                                 padding=True, return_tensors="pt").to(self.device)
            probs = torch.softmax(self.model(**enc).logits.float(), dim=-1)[:, PHISHING_ID]
            out.extend(probs.cpu().tolist())
        return out

    def score_email(self, subject: str, body_text: str = "", body_html: str = "") -> tuple[float, str]:
        """Returns (phishing probability, the cleaned text the model saw)."""
        text = email_text(subject, body_text, body_html)
        return self.predict_cleaned([text])[0], text
