"""Audit the Zenodo validation set: size, labels, and how templated it is."""
from pathlib import Path

import pandas as pd

path = next((Path(__file__).parent / "data").glob("Phishing_validation*.csv"))
d = pd.read_csv(path)
text = d["Email Text"].fillna("").astype(str)

print("rows:", len(d), "| labels:", d["Email Type"].value_counts().to_dict())
print("exact duplicates:", int(text.duplicated().sum()))
# mask the greeting name so "Dear Jordan" and "Dear Sam" count as one template
masked = text.str.replace(r"^(Dear|Hi|Hello)\s+\w+", r"\1 NAME", regex=True)
print("distinct after masking the greeting name:", masked.nunique())
print("median words:", int(text.str.split().str.len().median()))