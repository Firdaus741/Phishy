# Phishy

Final year project (UiTM, Computer Networks): a mobile app that reads a user's Gmail inbox and flags phishing emails using a fine-tuned DistilBERT model plus URL and email-header checks.

## Stack
- Flutter mobile app (`mobile/`, not started)
- Python FastAPI backend (`backend/`)
- DistilBERT text classifier, fine-tuned locally on a laptop RTX 3050 (6 GB VRAM) (`ml/`)
- Gmail API (OAuth2, read-only), VirusTotal API (URL reputation only), SPF/DKIM/DMARC results from the Authentication-Results header, Firebase Cloud Messaging for push alerts
- Two verdicts only: Safe, Phishing (no "Suspicious" band, to keep evaluation simple). The model outputs a phishing probability; the verdict combines it with the URL and header signals using one cutoff (still to be defined).

## Layout
- `ml/`: audit scripts, `text_cleaning.py` (shared `clean()` and `dedupe_key()`), `prepare_data.py` (older 5-source split in `ml/data/processed/`, no longer used for training), `build_unified.py` (unified schema, writes `ml/data/unified/`), `train.py` (fine-tunes any Hugging Face model on `unified.csv`, English rows, writes `ml/out/<model>/metrics.json` + `errors.csv`, saves the model to `backend/models/<model>`), `benchmark.py` (`baselines`, `loso`, `latency` commands, writes `ml/out/benchmark/`)
- `ml/Training Result/`: pasted terminal logs of each run, kept as evidence for Chapter 4
- `ml/data/unified/`: `unified.csv` (text, label, category, source, language, split), `external_zenodo.csv` (external check only, never trained on), `source_report.csv` (per-source format and rows kept, for Chapter 4)
- `backend/`: `main.py` (FastAPI, `/health`), `gmail_client.py` (login, fetch, parse emails incl. Reply-To and Return-Path), `header_checks.py` (rule-based SPF/DKIM/DMARC, Reply-To and brand-impersonation checks; `suspicious` = auth failed or brand mismatch, Reply-To mismatch is a weak signal), `test_header_checks.py` (run: `python backend\test_header_checks.py`), `classifier.py` (loads DistilBERT once, scores emails with the shared `clean()`), `analysis.py` (the one `analyze()` used by `/predict` and the scan script), `scan_inbox.py` (run the full analysis on your own Gmail, read-only: `python backend\scan_inbox.py [--count N] [--label SPAM] [--vt]`; VirusTotal off unless `--vt`), `link_checks.py` (extract links, local rules, VirusTotal lookup with sqlite cache and rate limit), `test_predict.py`, `test_link_checks.py` (mocked VirusTotal, no key needed). Secrets go in `backend/.env` (copy `backend/.env.example`; git-ignored).
- `ml/data/`, `ml/out/`, `backend/models/` are git-ignored

## Environment (Windows, PowerShell, project on D:\Phishy)
- Always activate the venv: `.\.venv\Scripts\Activate.ps1` (prompt must start with `(.venv)`). In cmd: `.venv\Scripts\activate.bat`. A ModuleNotFoundError for numpy, google or torch almost always means the venv is not active.
- PyTorch is the CUDA 12.6 build: `pip install torch --index-url https://download.pytorch.org/whl/cu126`
- C: is nearly full. Caches live on D: (`PIP_CACHE_DIR=D:\cache\pip`, `HF_HOME=D:\cache\huggingface`). In each new terminal run `$env:TEMP="D:\temp"; $env:TMP="D:\temp"` before big installs.
- Run: `python backend\gmail_client.py`, `cd backend; python -m uvicorn main:app --reload`, `python ml\build_unified.py`, `python ml\train.py --quick`, then `python ml\train.py [hf-model-name]`; `python ml\benchmark.py baselines|loso [--model NAME]|latency`
- On CUDA out of memory, lower `per_device_train_batch_size` (16 to 8).
- Hugging Face downloads can hang silently (Xet 404): set `$env:HF_HUB_DISABLE_XET="1"` and `$env:HF_HOME="D:\cache\huggingface"` first. A new terminal tab needs the venv activated again.

## Rules
- Never commit or print secrets: `credentials.json`, `token.json`, `.env`. Check `git status` before every commit.
- Keep the Gmail scope read-only. The Google app is in Testing mode, so `backend/token.json` expires after about 7 days: delete it and log in again.
- Labels: 0 = legit, 1 = phishing.
- The text cleaning (`clean()` in `ml/text_cleaning.py`) must be applied identically at inference time. Training, the data scripts and the backend must all import it from there; never copy it. The backend needs `ml/` on the Python path to import it.
- Read SPF/DKIM/DMARC from the topmost Authentication-Results header (added by Gmail's own server), never from sender-controlled headers.
- VirusTotal's free tier is rate limited (about 4 requests per minute): cache results and cap URLs per email.

## Data caveats (state these in the report)
- Phishing class = Nazario + Nigerian_Fraud (about 4,650 emails, mostly advance-fee fraud). Legit class in `unified.csv` = capped label-0 rows from Enron, SpamAssassin, CEAS_08, Ling and TREC_05 (9,500 emails); the older `processed/` split uses only the first three. Spam-labelled rows are excluded on purpose.
- Only 2 phishing sources (very different: advance-fee fraud vs credential phishing), so models learn source style. Leave-one-source-out confirms it: see Results. More phishing sources is the biggest improvement left.
- TREC_05.csv is malformed: `build_unified.py` falls back to a slower parser that skips bad lines.
- Nazario "folder internal data" mail-server messages are filtered out as junk.
- Dataset provenance (source URL, download date, licence, SHA-256) is still to be recorded for Chapter 4. Enron contains real people's emails (ethics note).
- The test split is in-distribution, so its scores overstate real-world accuracy. Real checks: the user's own inbox and a held-out-source experiment.
- `Phishing_validation_emails.csv` has only about 100 unique emails (28 templates): smoke test only.
- `malay_phishing.csv` is about 56 templates and every phishing row contains a link: demo slice only, never a headline metric.
- `malicious_phish.csv` (URLs) is parked and not used by the email model.

## Academic constraints
- Cite peer-reviewed sources only (no blogs or marketing statistics). DistilBERT is deep learning, not classical machine learning. VirusTotal checks URLs only, not headers. Train and test data must stay separate.
- Writing: concise, plain language, short paragraphs, comparison tables for technical content.

## Results so far (single seed, English `unified.csv`, 1,415 test emails; 1 email = 0.07%)
In-distribution test (random split). All models are within a few emails of each other; GPU run-to-run noise is about 1 email (BERT-base retrained: F1 0.9902 then 0.9892), so do not rank models by these.

| Model | Params | Test F1 | Wrong | Train time | CPU ms/email | Size MB |
|---|---|---|---|---|---|---|
| DistilBERT | 67.0M | 0.9902 | 9 | 5.1 min | 91 | 268 |
| BERT-base | 109.5M | 0.9892 | 10 | 10.7 min | 178 | 438 |
| MiniLM-L12 | 33.4M | 0.9892 | 10 | 4.3 min | 59 | 134 |
| RoBERTa-base | 124.6M | 0.9881 | 11 | 10.2 min | 176 | 499 |
| ELECTRA-small | 13.5M | 0.9827 | 16 | 2.4 min | 35 | 54 |
| TF-IDF + Linear SVM | n/a | 0.9881 | 11 | 8 s | 0.9 | 10 |
| TF-IDF + Logistic Regression | n/a | 0.9859 | 13 | 9 s | 1.1 | 10 |
| TF-IDF + Naive Bayes | n/a | 0.9870 | 12 | 7 s | 2.0 | 16 |

Four test emails are wrong in every model (ambiguous or poorly labelled), so the ceiling is about 99.7%.

Leave-one-source-out (model trained WITHOUT the source, accuracy on that source). Phishing rows are detection rate:

| Held out | TF-IDF LogReg | ELECTRA-small | MiniLM-L12 | DistilBERT |
|---|---|---|---|---|
| nazario (phishing) | 3.7% | 26.1% | 23.9% | 30.0% |
| nigerian (phishing) | 0.5% | 2.1% | 9.1% | 7.9% |
| 5 legit sources (range) | 98.3-99.8% | 97.1-99.3% | 97.5-99.2% | 98.3-99.7% |
| 5 legit sources (mean) | 99.2% | 98.2% | 98.7% | 98.8% |

Reading: transformers generalise better than TF-IDF to unseen phishing, DistilBERT beats ELECTRA on all 7 folds, but every model misses most unseen phishing. DistilBERT vs MiniLM is a near tie (DistilBERT ahead on Nazario, MiniLM ahead on Nigerian and on 3 of 5 legit sources), so do not claim DistilBERT generalises better than MiniLM. MiniLM is faster (59 vs 91 ms) and half the size; state this as an honest alternative. With only 2 phishing sources, holding one out leaves one phishing source in training (harshest test), so this shows thin data as much as model limits. State this in the report. The header and URL checks matter because the text model alone will not generalise. CPU latency absolute values vary about 30% with machine load; ratios are stable (DistilBERT about 2x faster than BERT/RoBERTa).

## Status (update as you go)
- Done: environment, Gmail client, FastAPI `/health`, data audit, shared `clean()` module, unified dataset (14,150 English emails), 5 Hugging Face models trained, TF-IDF baselines, leave-one-source-out for TF-IDF, ELECTRA, MiniLM and DistilBERT, CPU latency.
- In progress: Chapter 4 evidence. Still missing: more phishing sources then rerun leave-one-source-out, several seeds, provenance table (URL, date, licence, SHA-256).
- Header checks done: unit-tested (12 tests) and run on 10 real inbox emails (all Gmail-verified, all pass, no false flags). No real failure case seen yet (test on the Spam folder). The brand list in `header_checks.py` is short and illustrative: verify and extend it.
- `/predict` done (`backend/classifier.py`, `backend/main.py`): loads `backend/models/distilbert-base-uncased` once at startup, uses the shared `clean()`, returns text probability + header result. `text_label` uses a placeholder 0.5 cutoff (env `PHISHY_TEXT_THRESHOLD`); the final verdict is not built yet. The backend scores the 1,415 test emails with exactly the same 9 errors as the training run. Run: `cd backend; python -m uvicorn main:app --reload`; tests: `cd backend; python test_predict.py`.
- Link checks done and tested with a mocked VirusTotal (19 tests); NOT yet run against the real VirusTotal (needs the user's own free API key in `backend/.env`). Rules: links are never opened; VirusTotal is lookup-only (unknown URLs are not submitted); only scheme+host+path is sent (query/fragment dropped for privacy, `VT_STRIP_QUERY=false` to change; fewer exact matches); max 3 links per email (`VT_MAX_URLS`), chosen by priority (strong local flag, then a domain different from the sender's, then the rest); 4 requests/minute then "unchecked" (no waiting); 60 s back-off after a 429; daily cap 450 counted in the sqlite file so it survives restarts (`VT_DAILY_CAP`, the key's real limit is 500/day); 24 h cache (cache hits cost no quota); `/health` shows `requests_today`; 2+ engines = malicious, 1 = suspicious (VirusTotal has false positives). Local strong flags: IP host, punycode, user@ in URL, link text showing a different domain than the target. `/predict` now returns `links` too.
- Next: verdict decision rule (combine text, headers, links into Safe/Phishing), VirusTotal check with caching, optional local URL classifier from `malicious_phish.csv`, verdict fusion (hand-set rule, tested on own mail since no dataset has text + headers + links), FCM, Flutter app. Commit and push the new `ml/` scripts and `Progress.md` (remote `origin` = `Firdaus741/Phishy` is set; nothing pushed since the Oct 14 commit).

## Working style
- Explain what each command does and go one step at a time. Say so directly when something looks wrong.