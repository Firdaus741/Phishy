PS D:\Phishy> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\Phishy\.venv\Scripts\Activate.ps1)
(.venv) PS D:\Phishy> python ml\train.py --quick

=== DATA CHECK ===
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=  400  legit=  262  phishing=  138
val   rows=  100  legit=   64  phishing=   36
test  rows=  100  legit=   67  phishing=   33
Train/test overlap: none (checked)

Model: distilbert-base-uncased | quick mode: True
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Loading weights: 100%|█| 100/100 [00:00<
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
vocab_transform.bias    | UNEXPECTED | 
classifier.bias         | MISSING    | 
pre_classifier.bias     | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'eval_loss': '0.6739', 'eval_accuracy': '0.67', 'eval_precision': '0.8', 'eval_recall': '0.1111', 'eval_f1': '0.1951', 'eval_runtime': '0.3016', 'eval_samples_per_second': '331.6', 'eval_steps_per_second': '13.26', 'epoch': '1'}
Writing model shards: 100%|█| 1/1 [00:00
{'train_runtime': '5.618', 'train_samples_per_second': '71.2', 'train_steps_per_second': '2.314', 'train_loss': '1.317', 'epoch': '1'}
100%|███| 13/13 [00:05<00:00,  2.21it/s]
Writing model shards: 100%|█| 1/1 [00:00
100%|█████| 4/4 [00:00<00:00, 17.72it/s]

=== TEST RESULTS ===
{
  "model": "distilbert-base-uncased",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 400,
    "val": 100,
    "test": 100
  },
  "accuracy": 0.66,
  "precision": 0.3333333333333333,
  "recall": 0.030303030303030304,
  "f1": 0.05555555555555555,
  "false_positive_rate": 0.029850746268656716,
  "confusion": {
    "tn": 65,
    "fp": 2,
    "fn": 32,
    "tp": 1
  }
}

Accuracy by source:
  ceas_ham           n=  12  accuracy=1.000
  enron_ham          n=  25  accuracy=0.960
  ling_ham           n=  11  accuracy=1.000
  nazario            n=  11  accuracy=0.000
  nigerian           n=  22  accuracy=0.045
  spamassassin_ham   n=  11  accuracy=1.000
  trec_ham           n=   8  accuracy=0.875