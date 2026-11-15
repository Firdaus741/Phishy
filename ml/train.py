"""Fine-tune a Hugging Face model on the UNIFIED English email data and evaluate on its test split.

Data: ml/data/unified/unified.csv (English rows only; the 'split' column gives train/val/test).

Usage:
  python ml\\train.py --quick                       # 1-minute pipeline check (DistilBERT)
  python ml\\train.py                               # full run, DistilBERT
  python ml\\train.py roberta-base                  # any Hugging Face model name
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)

ROOT = Path(__file__).resolve().parent.parent
UNIFIED_CSV = ROOT / "ml" / "data" / "unified" / "unified.csv"
CLI = [a for a in sys.argv[1:] if not a.startswith("--")]
MODEL_NAME = CLI[0] if CLI else "distilbert-base-uncased"
QUICK = "--quick" in sys.argv
TAG = MODEL_NAME.split("/")[-1]
RUN_DIR = ROOT / "ml" / "out" / (TAG + "_quick" if QUICK else TAG)  # quick runs never overwrite real results
OUT_DIR = RUN_DIR / "quick_model" if QUICK else ROOT / "backend" / "models" / TAG
MAX_LEN = 256
SEED = 42


class EmailDataset(torch.utils.data.Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.enc = tokenizer(list(texts), truncation=True, max_length=MAX_LEN)
        self.labels = [int(x) for x in labels]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        item = {k: v[i] for k, v in self.enc.items()}
        item["labels"] = self.labels[i]
        return item


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    p, r, f1, _ = precision_recall_fscore_support(
        labels, preds, average="binary", zero_division=0
    )
    return {"accuracy": accuracy_score(labels, preds), "precision": p, "recall": r, "f1": f1}


def main():
    set_seed(SEED)
    df = pd.read_csv(UNIFIED_CSV)
    df = df[df["language"] == "en"]  # Malay is excluded: it is ~56 templates (see Progress.md)
    train, val, test = (df[df["split"] == s].reset_index(drop=True) for s in ("train", "val", "test"))
    if QUICK:
        train, val, test = train.sample(400, random_state=SEED), val.sample(100, random_state=SEED), test.sample(100, random_state=SEED)

    # Proof of what is being trained on
    print("\n=== DATA CHECK ===")
    print("File:", UNIFIED_CSV)
    print("Sources in train:", sorted(train["source"].unique()))
    for name, part in (("train", train), ("val", val), ("test", test)):
        print(f"{name:5s} rows={len(part):5d}  legit={int((part.label == 0).sum()):5d}  phishing={int((part.label == 1).sum()):5d}")
    assert not set(train["text"]) & set(test["text"]), "train and test share identical texts"
    print("Train/test overlap: none (checked)\n")
    print("Model:", MODEL_NAME, "| quick mode:", QUICK)
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "NONE (CPU only)")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=2,
        id2label={0: "legit", 1: "phishing"},
        label2id={"legit": 0, "phishing": 1},
    )
    train_ds = EmailDataset(train["text"], train["label"], tokenizer)
    val_ds = EmailDataset(val["text"], val["label"], tokenizer)
    test_ds = EmailDataset(test["text"], test["label"], tokenizer)

    args = TrainingArguments(
        output_dir=str(RUN_DIR),
        num_train_epochs=1 if QUICK else 3,
        per_device_train_batch_size=16,   # drop to 8 if you get an out-of-memory error
        gradient_accumulation_steps=2,
        per_device_eval_batch_size=32,
        learning_rate=2e-5,
        weight_decay=0.01,
        warmup_steps=100,
        fp16=torch.cuda.is_available(),
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        logging_steps=25,
        report_to="none",
        seed=SEED,
    )
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=compute_metrics,
    )
    trainer.train()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(OUT_DIR))
    tokenizer.save_pretrained(str(OUT_DIR))

    # Final evaluation on the held-out test split
    logits = trainer.predict(test_ds).predictions
    probs = torch.softmax(torch.tensor(logits), dim=-1)[:, 1].numpy()
    preds = (probs >= 0.5).astype(int)
    y = test["label"].to_numpy()
    p, r, f1, _ = precision_recall_fscore_support(y, preds, average="binary", zero_division=0)
    tn, fp, fn, tp = confusion_matrix(y, preds).ravel()
    result = {
        "model": MODEL_NAME,
        "data_file": str(UNIFIED_CSV),
        "rows": {"train": len(train), "val": len(val), "test": len(test)},
        "accuracy": float(accuracy_score(y, preds)),
        "precision": float(p),
        "recall": float(r),
        "f1": float(f1),
        "false_positive_rate": float(fp / (fp + tn)),
        "confusion": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)},
    }
    print("\n=== TEST RESULTS ===")
    print(json.dumps(result, indent=2))

    test = test.assign(prob_phishing=probs, pred=preds)
    print("\nAccuracy by source:")
    for src, g in test.groupby("source"):
        print(f"  {src:18s} n={len(g):4d}  accuracy={(g.pred == g.label).mean():.3f}")

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    (RUN_DIR / "metrics.json").write_text(json.dumps(result, indent=2))
    test[test.pred != test.label].to_csv(RUN_DIR / "errors.csv", index=False)
    print("\nSaved model to:", OUT_DIR)


if __name__ == "__main__":
    main()