"""Quick audit of the four datasets: size, labels, duplicates, empties, lengths."""
from pathlib import Path

import pandas as pd
import re
from pathlib import Path

DATA = Path(__file__).parent / "data"

# Edit these file names to match what you copied into ml/data/
MALAY = DATA / "malay_phishing.csv"      # text, label
SPAMASSASSIN = DATA / "SpamAssasin.csv" # sender, ..., subject, body, label, urls
CEAS = DATA / "CEAS_08.csv"              # same columns as above
URLS = DATA / "malicious_phish.csv"      # url, type

def normalise(s):
    s = re.sub(r"https?://\S+", "URL", s)
    return re.sub(r"\d+", "0", s)


def report(name, text, label):
    text = text.fillna("").astype(str).str.strip()
    dup = text.duplicated()
    words = text.str.split().str.len()
    print(f"\n=== {name} ===")
    print("rows:", len(text))
    print("labels:", label.value_counts().to_dict())
    print("empty texts:", int((text == "").sum()))
    print("duplicate texts:", int(dup.sum()), f"({dup.mean():.1%})")
    print("distinct after masking numbers and URLs:", text.map(normalise).nunique())
    print("words per text: median", int(words.median()), "| 95th pct", int(words.quantile(0.95)))

m = pd.read_csv(MALAY, encoding="utf-8-sig")
report("Malay", m["text"], m["label"])

for name, path in [("SpamAssassin", SPAMASSASSIN), ("CEAS_08", CEAS)]:
    d = pd.read_csv(path)
    text = d["subject"].fillna("").astype(str) + "\n" + d["body"].fillna("").astype(str)
    report(name, text, d["label"])

u = pd.read_csv(URLS)
print("\n=== URLs ===")
print("rows:", len(u), "| types:", u["type"].value_counts().to_dict())
print("duplicate urls:", int(u["url"].duplicated().sum()))