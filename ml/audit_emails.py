"""Audit every email CSV in ml/data that has subject, body and label columns."""
import re
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"


def normalise(s):
    s = re.sub(r"https?://\S+", "URL", s)
    return re.sub(r"\d+", "0", s)


for path in sorted(DATA.glob("*.csv")):
    head = pd.read_csv(path, nrows=1)
    if not {"subject", "body", "label"} <= set(head.columns):
        print(f"\nskipping {path.name}: columns are {list(head.columns)}")
        continue
    d = pd.read_csv(path)
    body = d["body"].fillna("").astype(str)
    text = d["subject"].fillna("").astype(str) + "\n" + body
    html = body.str.contains("<html|<body|<div|<table", case=False).mean()
    print(f"\n=== {path.name} ===")
    print("rows:", len(d), "| labels:", d["label"].value_counts().to_dict())
    print("empty bodies:", int((body.str.strip() == "").sum()))
    print("distinct after masking:", text.map(normalise).nunique())
    print("median words:", int(text.str.split().str.len().median()))
    print("bodies containing HTML tags:", f"{html:.1%}")