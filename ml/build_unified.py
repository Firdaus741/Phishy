"""Convert every raw dataset into ONE schema and write the train/val/test split.

Output (ml/data/unified/):
  unified.csv        text, label, category, source, language, split
  external_zenodo.csv  the templated Zenodo set, kept OUT of training (external check only)
  source_report.csv  one row per source: original format, label meaning, rows kept (for Chapter 4)

Schema
  label     1 = phishing/fraud, 0 = legitimate
  category  phishing | fraud | ham
  source    which raw file it came from (used for leave-one-source-out tests)
  language  en | ms
"""
import re
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from text_cleaning import clean, dedupe_key

DATA = Path(__file__).parent / "data"
OUT = DATA / "unified"
OUT.mkdir(exist_ok=True)
SEED = 42

# (file, label value to keep, category, cap, source, note on original format)
EMAIL_SOURCES = [
    ("Nazario.csv", 1, "phishing", None, "nazario", "sender,receiver,date,subject,body,urls,label; label 1 = phishing"),
    ("Nigerian_Fraud.csv", 1, "fraud", None, "nigerian", "same columns; label 1 = advance-fee fraud"),
    ("Enron.csv", 0, "ham", 3000, "enron_ham", "subject,body,label; only legitimate rows kept"),
    ("SpamAssasin.csv", 0, "ham", 2000, "spamassassin_ham", "full headers; label 1 = SPAM (not phishing), so only ham kept"),
    ("CEAS_08.csv", 0, "ham", 1500, "ceas_ham", "full headers; label 1 = SPAM (not phishing), so only ham kept"),
    ("Ling.csv", 0, "ham", 1500, "ling_ham", "subject,body,label; label 1 = spam, so only ham kept"),
    ("TREC_05.csv", 0, "ham", 1500, "trec_ham", "full headers; label 1 = spam, so only ham kept"),
]
JUNK_SUBJECT = re.compile(r"folder internal data|mail system internal data", re.I)


def tidy(d: pd.DataFrame, label: int, category: str, source: str, language: str, cap=None) -> pd.DataFrame:
    d = d[d["text"].str.split().str.len() >= 5].copy()
    d["key"] = d["text"].map(dedupe_key)
    d = d.drop_duplicates("key")
    if cap and len(d) > cap:
        d = d.sample(cap, random_state=SEED)
    d["label"], d["category"], d["source"], d["language"] = label, category, source, language
    return d[["text", "label", "category", "source", "language", "key"]]


frames, report = [], []

for file, keep, category, cap, source, note in EMAIL_SOURCES:
    try:
        d = pd.read_csv(DATA / file, usecols=["subject", "body", "label"])
    except pd.errors.ParserError:  # malformed file (TREC_05): slower tolerant parser, bad lines skipped
        d = pd.read_csv(DATA / file, usecols=["subject", "body", "label"], engine="python", on_bad_lines="skip")
    raw_rows = len(d)
    d = d[pd.to_numeric(d["label"], errors="coerce") == keep].copy()  # misparsed rows become NaN and drop out
    subj = d["subject"].fillna("").astype(str)
    d = d[~subj.str.contains(JUNK_SUBJECT)]
    d["text"] = [
        clean(str(s) if pd.notna(s) else "", str(b) if pd.notna(b) else "")
        for s, b in zip(d["subject"], d["body"])
    ]
    out = tidy(d, 1 if keep == 1 else 0, category, source, "en", cap)
    frames.append(out)
    report.append({"source": source, "file": file, "raw_rows": raw_rows, "kept": len(out), "language": "en", "original_format": note})
    print(f"{source}: raw {raw_rows} -> kept {len(out)}")

# Malay: text + text label
m = pd.read_csv(DATA / "malay_phishing.csv", encoding="utf-8-sig")
m["text"] = m["text"].fillna("").astype(str).map(lambda t: re.sub(r"\s+", " ", re.sub(r"https?://\S+|www\.\S+", " [URL] ", t)).strip())
for lab, cat, val in [("phishing", "phishing", 1), ("legit", "ham", 0)]:
    part = m[m["label"] == lab]
    out = tidy(part, val, cat, f"malay_{lab}", "ms")
    frames.append(out)
    report.append({"source": f"malay_{lab}", "file": "malay_phishing.csv", "raw_rows": len(part), "kept": len(out), "language": "ms", "original_format": "text,label ('phishing'/'legit'), SMS-style short messages"})
    print(f"malay_{lab}: kept {len(out)}")

df = pd.concat(frames, ignore_index=True)
conflict = df.groupby("key")["label"].nunique()
n_conf = int((conflict > 1).sum())
df = df[~df["key"].isin(conflict[conflict > 1].index)].drop_duplicates("key").drop(columns="key")
print(f"\nremoved {n_conf} texts that appear under both labels")

strat = df["label"].astype(str) + df["source"]
train, rest = train_test_split(df, test_size=0.2, stratify=strat, random_state=SEED)
val, test = train_test_split(rest, test_size=0.5, stratify=rest["label"].astype(str) + rest["source"], random_state=SEED)
df = pd.concat([train.assign(split="train"), val.assign(split="val"), test.assign(split="test")], ignore_index=True)
df.to_csv(OUT / "unified.csv", index=False)

# Zenodo: highly templated, so use ONLY as an external sanity check
z = pd.read_csv(next(DATA.glob("Phishing_validation*.csv")))
z = pd.DataFrame({
    "text": z["Email Text"].fillna("").astype(str),
    "label": (z["Email Type"] == "Phishing Email").astype(int),
})
z["source"], z["language"] = "zenodo_external", "en"
z.to_csv(OUT / "external_zenodo.csv", index=False)
report.append({"source": "zenodo_external", "file": "Phishing_validation_emails.csv", "raw_rows": len(z), "kept": len(z), "language": "en", "original_format": "'Email Text','Email Type' ('Safe Email'/'Phishing Email'); templated, external test only"})

pd.DataFrame(report).to_csv(OUT / "source_report.csv", index=False)

print("\n=== unified.csv ===")
print(df.groupby(["language", "label"]).size().to_string())
print()
print(df.groupby(["split", "label"]).size().unstack().to_string())
print()
print(df.groupby(["source", "label", "split"]).size().unstack().to_string())

# Link-shortcut check for Malay: does 'has [URL]' alone separate the classes?
ms = df[df["language"] == "ms"]
print("\nMalay share containing a link, by label:",
      ms.assign(link=ms["text"].str.contains(r"\[URL\]")).groupby("label")["link"].mean().round(3).to_dict())
