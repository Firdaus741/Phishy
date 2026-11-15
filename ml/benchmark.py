"""Chapter 4 extras that train.py does not cover. Three separate commands:

  python ml\\benchmark.py baselines
      Classical TF-IDF models (Logistic Regression, Linear SVM, Naive Bayes) on the SAME
      unified split. Writes ml/out/<name>/metrics.json + errors.csv, like train.py does.

  python ml\\benchmark.py loso [--model distilbert-base-uncased] [--epochs 2] [--smoke]
      Leave-one-source-out: for each source, train WITHOUT it and test on it. Always runs
      TF-IDF + Logistic Regression; also fine-tunes the Hugging Face model if --model is given.
      Shows accuracy on the unseen source next to the normal in-distribution accuracy.

  python ml\\benchmark.py latency
      CPU time per email (tokenise + predict, one email at a time) and size on disk for every
      model in backend/models plus the classical baselines.

Results are printed and saved as CSV in ml/out/benchmark/.
"""
import argparse
import gc
import json
import pickle
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

ROOT = Path(__file__).resolve().parent.parent
UNIFIED_CSV = ROOT / "ml" / "data" / "unified" / "unified.csv"
OUT = ROOT / "ml" / "out"
BENCH = OUT / "benchmark"
MODELS = ROOT / "backend" / "models"
SEED = 42
MAX_LEN = 256
CLASSICAL = ["tfidf_logreg", "tfidf_linsvm", "tfidf_nb"]


def load() -> pd.DataFrame:
    df = pd.read_csv(UNIFIED_CSV)
    return df[df["language"] == "en"].reset_index(drop=True)  # Malay excluded, see Progress.md


def classical(name: str):
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True, max_features=200_000)
    clf = {
        "tfidf_logreg": LogisticRegression(max_iter=2000, C=10),
        "tfidf_linsvm": LinearSVC(C=1.0, random_state=SEED),
        "tfidf_nb": ComplementNB(),
    }[name]
    return make_pipeline(vec, clf)


# ----------------------------------------------------------------------------- baselines
def cmd_baselines(_args):
    df = load()
    train, test = df[df.split == "train"], df[df.split == "test"]
    print(f"Data: {UNIFIED_CSV}\ntrain={len(train)} test={len(test)} (English only)\n")
    rows = []
    for name in CLASSICAL:
        t0 = time.perf_counter()
        model = classical(name).fit(train["text"], train["label"])
        train_s = time.perf_counter() - t0
        pred = model.predict(test["text"])
        y = test["label"].to_numpy()
        p, r, f1, _ = precision_recall_fscore_support(y, pred, average="binary", zero_division=0)
        tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
        result = {
            "model": name, "data_file": str(UNIFIED_CSV),
            "rows": {"train": len(train), "val": int((df.split == "val").sum()), "test": len(test)},
            "accuracy": float(accuracy_score(y, pred)), "precision": float(p), "recall": float(r),
            "f1": float(f1), "false_positive_rate": float(fp / (fp + tn)),
            "confusion": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)},
            "train_seconds": round(train_s, 1),
        }
        run_dir = OUT / name
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "metrics.json").write_text(json.dumps(result, indent=2))
        prob = model.predict_proba(test["text"])[:, 1] if hasattr(model, "predict_proba") else np.nan
        bad = test.assign(prob_phishing=prob, pred=pred)
        bad[bad.pred != bad.label][["text", "label", "source", "prob_phishing", "pred"]].to_csv(
            run_dir / "errors.csv", index=False)
        rows.append({"model": name, "acc": result["accuracy"], "prec": p, "rec": r, "f1": f1,
                     "fpr": result["false_positive_rate"], "fp": fp, "fn": fn,
                     "wrong": int(fp + fn), "train_s": round(train_s, 1)})
    print(pd.DataFrame(rows).round(4).to_string(index=False))


# ----------------------------------------------------------------------------- leave-one-source-out
def make_transformer_fit_predict(model_name: str, epochs: int):
    import torch
    from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                              DataCollatorWithPadding, Trainer, TrainingArguments, set_seed)

    class DS(torch.utils.data.Dataset):
        def __init__(self, texts, labels, tok):
            self.enc = tok(list(texts), truncation=True, max_length=MAX_LEN)
            self.labels = [int(x) for x in labels]

        def __len__(self):
            return len(self.labels)

        def __getitem__(self, i):
            item = {k: v[i] for k, v in self.enc.items()}
            item["labels"] = self.labels[i]
            return item

    def fit_predict(tr, te):
        set_seed(SEED)
        tok = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        args = TrainingArguments(
            output_dir=str(BENCH / "_tmp"), num_train_epochs=epochs,
            per_device_train_batch_size=16, gradient_accumulation_steps=2,
            per_device_eval_batch_size=32, learning_rate=2e-5, weight_decay=0.01,
            warmup_steps=100, fp16=torch.cuda.is_available(), eval_strategy="no",
            save_strategy="no", logging_steps=100, report_to="none", seed=SEED)
        trainer = Trainer(model=model, args=args, train_dataset=DS(tr["text"], tr["label"], tok),
                          data_collator=DataCollatorWithPadding(tok))
        trainer.train()
        pred = trainer.predict(DS(te["text"], te["label"], tok)).predictions.argmax(-1)
        del trainer, model
        gc.collect()
        torch.cuda.empty_cache()
        return pred

    return fit_predict


def in_distribution_accuracy(tag: str, df: pd.DataFrame) -> dict:
    """Per-source accuracy of the normal run (from its errors.csv), for comparison."""
    path = OUT / tag / "errors.csv"
    if not path.exists():
        return {}
    n = df[df.split == "test"].groupby("source").size()
    wrong = pd.read_csv(path).groupby("source").size().reindex(n.index, fill_value=0)
    return (1 - wrong / n).to_dict()


def loso(label: str, tag: str, fit_predict, df: pd.DataFrame, smoke: bool):
    seen = in_distribution_accuracy(tag, df)
    label_of = df.groupby("source")["label"].first()
    rows = []
    for held in sorted(df["source"].unique()):
        train = df[(df.source != held) & (df.split == "train")]
        test = df[df.source == held]  # every row of the held-out source: the model never saw it
        if smoke:
            train, test = train.sample(min(300, len(train)), random_state=SEED), test.sample(min(100, len(test)), random_state=SEED)
        t0 = time.perf_counter()
        pred = np.asarray(fit_predict(train, test))
        acc = float((pred == test["label"].to_numpy()).mean())
        rows.append({
            "held_out": held,
            "measures": "phishing recall" if label_of[held] == 1 else "legit specificity",
            "n": len(test), "unseen_acc": round(acc, 4),
            "normal_acc": round(seen[held], 4) if held in seen else np.nan,
            "seconds": round(time.perf_counter() - t0),
        })
        print(f"  [{label}] held out {held:18s} n={len(test):5d}  unseen={acc:.3f}", flush=True)
    res = pd.DataFrame(rows)
    res["drop"] = (res["normal_acc"] - res["unseen_acc"]).round(4)
    BENCH.mkdir(parents=True, exist_ok=True)
    res.to_csv(BENCH / f"loso_{tag}{'_smoke' if smoke else ''}.csv", index=False)
    print(f"\n=== Leave-one-source-out: {label} ===")
    print(res.to_string(index=False))
    print("(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)\n")


def cmd_loso(args):
    df = load()
    print(f"Data: {UNIFIED_CSV}\nsources: {sorted(df.source.unique())}\n")
    loso("tfidf_logreg", "tfidf_logreg", lambda tr, te: classical("tfidf_logreg").fit(tr["text"], tr["label"]).predict(te["text"]), df, args.smoke)
    if args.model:
        tag = args.model.split("/")[-1]
        loso(args.model, tag, make_transformer_fit_predict(args.model, 1 if args.smoke else args.epochs), df, args.smoke)


# ----------------------------------------------------------------------------- latency
def time_one_by_one(fn, texts, warmup=5):
    for t in texts[:warmup]:
        fn(t)
    ms = []
    for t in texts:
        t0 = time.perf_counter()
        fn(t)
        ms.append((time.perf_counter() - t0) * 1000)
    return float(np.median(ms)), float(np.percentile(ms, 95))


def cmd_latency(_args):
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    df = load()
    texts = df[df.split == "test"].sample(100, random_state=SEED)["text"].tolist()
    print(f"CPU only | torch threads: {torch.get_num_threads()} | 100 test emails, one at a time\n")
    rows = []
    train = df[df.split == "train"]
    for name in CLASSICAL:
        model = classical(name).fit(train["text"], train["label"])
        med, p95 = time_one_by_one(lambda t: model.predict([t]), texts)
        rows.append({"model": name, "type": "classical", "params_M": np.nan,
                     "size_MB": round(len(pickle.dumps(model)) / 1e6, 1),
                     "median_ms": round(med, 2), "p95_ms": round(p95, 2)})
    for d in sorted(p for p in MODELS.iterdir() if (p / "model.safetensors").exists()):
        tok = AutoTokenizer.from_pretrained(d)
        model = AutoModelForSequenceClassification.from_pretrained(d).to("cpu").eval()

        def run(t):
            with torch.inference_mode():
                model(**tok(t, truncation=True, max_length=MAX_LEN, return_tensors="pt"))

        med, p95 = time_one_by_one(run, texts)
        rows.append({"model": d.name, "type": "transformer", "params_M": round(model.num_parameters() / 1e6, 1),
                     "size_MB": round((d / "model.safetensors").stat().st_size / 1e6, 1),
                     "median_ms": round(med, 2), "p95_ms": round(p95, 2)})
        print(f"  done {d.name}", flush=True)
        del model
        gc.collect()
    res = pd.DataFrame(rows)
    BENCH.mkdir(parents=True, exist_ok=True)
    res.to_csv(BENCH / "latency.csv", index=False)
    print("\n" + res.to_string(index=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("baselines").set_defaults(fn=cmd_baselines)
    p = sub.add_parser("loso")
    p.add_argument("--model", help="Hugging Face model to fine-tune per fold, e.g. distilbert-base-uncased")
    p.add_argument("--epochs", type=int, default=2)
    p.add_argument("--smoke", action="store_true", help="tiny, fast pipeline check (numbers meaningless)")
    p.set_defaults(fn=cmd_loso)
    sub.add_parser("latency").set_defaults(fn=cmd_latency)
    a = ap.parse_args()
    a.fn(a)
