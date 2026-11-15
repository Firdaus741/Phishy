"""Build the cleaned, de-duplicated train/val/test split for the English email model."""
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from text_cleaning import clean, dedupe_key

DATA = Path(__file__).parent / "data"
OUT = DATA / "processed"
OUT.mkdir(exist_ok=True)
SEED = 42

# (file, keep only rows with this label, max rows to keep, short source name)
SOURCES = [
    ("Nazario.csv", 1, None, "nazario"),
    ("Nigerian_Fraud.csv", 1, None, "nigerian"),
    ("Enron.csv", 0, 3000, "enron_ham"),
    ("SpamAssasin.csv", 0, 2000, "spamassassin_ham"),
    ("CEAS_08.csv", 0, 1500, "ceas_ham"),
]


frames = []
for file, keep_label, cap, name in SOURCES:
    d = pd.read_csv(DATA / file, usecols=["subject", "body", "label"])
    d = d[d["label"] == keep_label].copy()
    d["text"] = [
        clean(str(s) if pd.notna(s) else "", str(b) if pd.notna(b) else "")
        for s, b in zip(d["subject"], d["body"])
    ]
    d = d[d["text"].str.split().str.len() >= 5].copy()
    d["key"] = d["text"].map(dedupe_key)
    d = d.drop_duplicates("key")
    if cap and len(d) > cap:
        d = d.sample(cap, random_state=SEED)
    d["source"] = name
    frames.append(d[["text", "label", "source", "key"]])
    print(f"{name}: kept {len(d)}")

df = pd.concat(frames, ignore_index=True)
# an email that appears under both labels is ambiguous, so drop it
conflict = df.groupby("key")["label"].nunique()
df = df[~df["key"].isin(conflict[conflict > 1].index)]
df = df.drop_duplicates("key").drop(columns="key")

strat = df["label"].astype(str) + df["source"]
train, rest = train_test_split(df, test_size=0.2, stratify=strat, random_state=SEED)
val, test = train_test_split(
    rest, test_size=0.5, stratify=rest["label"].astype(str) + rest["source"], random_state=SEED
)
for name, part in [("train", train), ("val", val), ("test", test)]:
    part.to_csv(OUT / f"{name}.csv", index=False)
    print(f"\n{name}: {len(part)} rows")
    print(part.groupby(["source", "label"]).size().to_string())