"""Look at what the labels really mean, and check for a link shortcut in the Malay data."""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"

for name, file in [("CEAS_08", "CEAS_08.csv"), ("SpamAssasin", "SpamAssasin.csv")]:
    d = pd.read_csv(DATA / file)
    for label in (0, 1):
        part = d[d["label"] == label]
        print(f"\n--- {name}, label {label}: 12 random subjects ---")
        for s in part["subject"].fillna("").sample(12, random_state=1):
            print("  *", str(s)[:80])
        domains = part["sender"].fillna("").str.extract(r"@([\w\.-]+)")[0].str.lower()
        print("top sender domains:", domains.value_counts().head(5).to_dict())

m = pd.read_csv(DATA / "malay_phishing.csv", encoding="utf-8-sig")
m["has_link"] = m["text"].str.contains("http", case=False)
print("\n--- Malay: share of messages containing a link, by label ---")
print(m.groupby("label")["has_link"].mean().round(3).to_dict())