"""Tests for /predict. Run from the backend folder: python test_predict.py

1. The endpoint works (sample emails, headers, errors).
2. The backend reproduces the training run: it scores the same 1,415 test emails as ml/train.py
   and should get (almost) the same wrong ones as ml/out/distilbert-base-uncased/errors.csv.
"""
from pathlib import Path

import pandas as pd
from fastapi.testclient import TestClient

from classifier import html_to_text
from main import app

client = None  # set by the runner below
ROOT = Path(__file__).resolve().parent.parent

NIGERIAN = (
    "URGENT BUSINESS PROPOSAL. I am the director of a bank in Abidjan. The sum of $10,500,000.00 "
    "was left by a late customer and nobody knows about it. I need your help to transfer the money "
    "to your account and you will receive 30 percent. Reply with your full name, telephone and address."
)
LEGIT = (
    "Hi team, attached is the agenda for tomorrow's project meeting at 10am in room 3. "
    "Please read the minutes from last week and send me any items you want to add. Thanks, Sarah"
)
GMAIL_FAIL = ("mx.google.com; dkim=fail header.i=@evil.com; spf=softfail smtp.mailfrom=x@evil.com; "
              "dmarc=fail (p=NONE) header.from=evil.com")


def test_html_to_text_keeps_links_and_drops_style():
    t = html_to_text('<style>p{color:red}</style><p>Click <a href="http://x.com/a">here</a></p>')
    assert "http://x.com/a" in t and "color" not in t and "<" not in t


def test_health():
    r = client.get("/health").json()
    assert r["status"] == "ok" and r["model_loaded"] and r["model"] == "distilbert-base-uncased"

def test_obvious_phishing_and_legit():
    p = client.post("/predict", json={"subject": "URGENT BUSINESS PROPOSAL", "body": NIGERIAN}).json()
    s = client.post("/predict", json={"subject": "Agenda", "body": LEGIT}).json()
    print(f"      nigerian-style p={p['phishing_probability']}  legit p={s['phishing_probability']}")
    assert p["text_label"] == "phishing" and s["text_label"] == "safe"

def test_html_only_email():
    r = client.post("/predict", json={"subject": "Agenda", "html": f"<html><body><p>{LEGIT}</p></body></html>"}).json()
    assert r["text_label"] == "safe"

def test_headers_come_back_with_the_prediction():
    r = client.post("/predict", json={"subject": "Hi", "body": LEGIT, "from": '"PayPal" <a@evil.com>',
                                      "authentication_results": GMAIL_FAIL}).json()
    assert r["headers"]["auth_failed"] and r["headers"]["suspicious"]

def test_links_come_back_with_the_prediction():
    html = '<p>Please confirm your login: <a href="http://evil.example/login">www.paypal.com</a></p>'
    r = client.post("/predict", json={"subject": "Confirm", "body": LEGIT, "html": html}).json()
    assert r["links"]["total_found"] == 1 and r["links"]["suspicious"]
    assert any("paypal.com" in x for x in r["links"]["reasons"])


def test_empty_email_is_rejected():
    assert client.post("/predict", json={"subject": "", "body": "   "}).status_code == 400

def test_matches_training_run():
    df = pd.read_csv(ROOT / "ml" / "data" / "unified" / "unified.csv")
    test = df[(df.language == "en") & (df.split == "test")].reset_index(drop=True)
    probs = app.state.clf.predict_cleaned(test["text"].tolist())  # texts are already cleaned
    pred = [int(p >= 0.5) for p in probs]
    wrong = {t for t, y, p in zip(test["text"], test["label"], pred) if y != p}
    trained = set(pd.read_csv(ROOT / "ml" / "out" / "distilbert-base-uncased" / "errors.csv")["text"])
    acc = 1 - len(wrong) / len(test)
    print(f"      backend: {len(wrong)} wrong of {len(test)} (acc {acc:.4f}) | training run: {len(trained)} wrong "
          f"| different: {len(wrong ^ trained)}")
    assert abs(len(wrong) - len(trained)) <= 2 and len(wrong ^ trained) <= 4


if __name__ == "__main__":
    import traceback

    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    failed = 0
    with TestClient(app) as client:  # keep the model loaded for the whole run
        globals()["client"] = client
        for n, f in tests:
            try:
                f()
                print("ok  ", n)
            except Exception:
                failed += 1
                print("FAIL", n)
                traceback.print_exc()
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
