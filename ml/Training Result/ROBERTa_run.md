(.venv) PS D:\Phishy> python ml\train.py roberta-base

=== DATA CHECK ===
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=11320  legit= 7600  phishing= 3720
val   rows= 1415  legit=  950  phishing=  465
test  rows= 1415  legit=  950  phishing=  465
Train/test overlap: none (checked)

Model: roberta-base | quick mode: False
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
tokenizer_config.json: 100%|█| 25.0/25.0 [00:0
D:\Phishy\.venv\Lib\site-packages\huggingface_hub\file_download.py:149: UserWarning: `huggingface_hub` cache-system uses symlinks by defaultto efficiently store duplicated files but yourmachine does not support them in D:\cache\huggingface\hub\models--roberta-base. Caching fileswill still work but in a degraded version thatmight require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)
Loading weights: 100%|█| 197/197 [00:00<00:00,
[transformers] RobertaForSequenceClassification LOAD REPORT from: roberta-base
Key                        | Status     | 
---------------------------+------------+-
lm_head.layer_norm.weight  | UNEXPECTED | 
lm_head.layer_norm.bias    | UNEXPECTED | 
lm_head.dense.weight       | UNEXPECTED | 
lm_head.bias               | UNEXPECTED | 
lm_head.dense.bias         | UNEXPECTED | 
classifier.out_proj.weight | MISSING    | 
classifier.dense.weight    | MISSING    | 
classifier.out_proj.bias   | MISSING    | 
classifier.dense.bias      | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.285', 'grad_norm': '3.254', 'learning_rate': '4.8e-06', 'epoch': '0.07062'}
{'loss': '1.08', 'grad_norm': '10.49', 'learning_rate': '9.8e-06', 'epoch': '0.1412'}
{'loss': '0.2818', 'grad_norm': '1.407', 'learning_rate': '1.48e-05', 'epoch': '0.2119'}
{'loss': '0.1299', 'grad_norm': '119.4', 'learning_rate': '1.98e-05', 'epoch': '0.2825'}
{'loss': '0.1777', 'grad_norm': '25.28', 'learning_rate': '1.95e-05', 'epoch': '0.3531'}
{'loss': '0.1251', 'grad_norm': '0.3158', 'learning_rate': '1.898e-05', 'epoch': '0.4237'}
{'loss': '0.04779', 'grad_norm': '33.64', 'learning_rate': '1.846e-05', 'epoch': '0.4944'}
{'loss': '0.06022', 'grad_norm': '34.67', 'learning_rate': '1.794e-05', 'epoch': '0.565'}
{'loss': '0.07132', 'grad_norm': '8.324', 'learning_rate': '1.742e-05', 'epoch': '0.6356'}
{'loss': '0.09213', 'grad_norm': '0.03217', 'learning_rate': '1.69e-05', 'epoch': '0.7062'}
{'loss': '0.1034', 'grad_norm': '0.0435', 'learning_rate': '1.638e-05', 'epoch': '0.7768'}
{'loss': '0.08163', 'grad_norm': '0.01752', 'learning_rate': '1.586e-05', 'epoch': '0.8475'}
{'loss': '0.042', 'grad_norm': '28.15', 'learning_rate': '1.534e-05', 'epoch': '0.9181'}
{'loss': '0.09111', 'grad_norm': '9.994', 'learning_rate': '1.482e-05', 'epoch': '0.9887'}
{'eval_loss': '0.0121', 'eval_accuracy': '0.9979', 'eval_precision': '0.9978', 'eval_recall':'0.9957', 'eval_f1': '0.9968', 'eval_runtime':'6.917', 'eval_samples_per_second': '204.6', 'eval_steps_per_second': '6.506', 'epoch': '1'}
Writing model shards: 100%|█| 1/1 [00:01<00:00
{'loss': '0.01812', 'grad_norm': '0.138', 'learning_rate': '1.43e-05', 'epoch': '1.059'}
{'loss': '0.01371', 'grad_norm': '0.01038', 'learning_rate': '1.378e-05', 'epoch': '1.13'}
{'loss': '0.09437', 'grad_norm': '0.04114', 'learning_rate': '1.326e-05', 'epoch': '1.201'}
{'loss': '0.06042', 'grad_norm': '98.67', 'learning_rate': '1.274e-05', 'epoch': '1.271'}
{'loss': '0.06679', 'grad_norm': '0.09784', 'learning_rate': '1.222e-05', 'epoch': '1.342'}
{'loss': '0.06956', 'grad_norm': '3.238', 'learning_rate': '1.17e-05', 'epoch': '1.412'}
{'loss': '0.02644', 'grad_norm': '1.609', 'learning_rate': '1.119e-05', 'epoch': '1.483'}
{'loss': '0.07716', 'grad_norm': '0.03411', 'learning_rate': '1.067e-05', 'epoch': '1.554'}
{'loss': '0.02378', 'grad_norm': '0.03862', 'learning_rate': '1.015e-05', 'epoch': '1.624'}
{'loss': '0.03422', 'grad_norm': '0.01743', 'learning_rate': '9.626e-06', 'epoch': '1.695'}
{'loss': '0.03517', 'grad_norm': '0.008036', 'learning_rate': '9.106e-06', 'epoch': '1.766'}
{'loss': '0.04817', 'grad_norm': '0.009185', 'learning_rate': '8.586e-06', 'epoch': '1.836'}
{'loss': '0.03469', 'grad_norm': '0.007634', 'learning_rate': '8.067e-06', 'epoch': '1.907'}
{'loss': '0.02686', 'grad_norm': '16', 'learning_rate': '7.547e-06', 'epoch': '1.977'}
{'eval_loss': '0.01497', 'eval_accuracy': '0.9979', 'eval_precision': '0.9978', 'eval_recall': '0.9957', 'eval_f1': '0.9968', 'eval_runtime': '6.744', 'eval_samples_per_second': '209.8', 'eval_steps_per_second': '6.672', 'epoch': '2'}
Writing model shards: 100%|█| 1/1 [00:01<00:00
{'loss': '0.06274', 'grad_norm': '0.09718', 'learning_rate': '7.027e-06', 'epoch': '2.048'}
{'loss': '0.004131', 'grad_norm': '0.04114', 'learning_rate': '6.507e-06', 'epoch': '2.119'}
{'loss': '0.01714', 'grad_norm': '0.01654', 'learning_rate': '5.988e-06', 'epoch': '2.189'}
{'loss': '0.000341', 'grad_norm': '0.05846', 'learning_rate': '5.468e-06', 'epoch': '2.26'}
{'loss': '0.01942', 'grad_norm': '0.006379', 'learning_rate': '4.948e-06', 'epoch': '2.331'}
{'loss': '0.0002927', 'grad_norm': '0.004465','learning_rate': '4.428e-06', 'epoch': '2.401'}
{'loss': '0.02245', 'grad_norm': '0.006185', 'learning_rate': '3.909e-06', 'epoch': '2.472'}
{'loss': '0.01961', 'grad_norm': '0.006712', 'learning_rate': '3.389e-06', 'epoch': '2.542'}
{'loss': '0.000246', 'grad_norm': '0.0291', 'learning_rate': '2.869e-06', 'epoch': '2.613'}
{'loss': '0.02125', 'grad_norm': '0.004556', 'learning_rate': '2.349e-06', 'epoch': '2.684'}
{'loss': '0.02907', 'grad_norm': '0.007888', 'learning_rate': '1.83e-06', 'epoch': '2.754'}
{'loss': '0.001359', 'grad_norm': '0.005758', 'learning_rate': '1.31e-06', 'epoch': '2.825'}
{'loss': '0.03992', 'grad_norm': '0.006118', 'learning_rate': '7.9e-07', 'epoch': '2.895'}
{'loss': '0.0002821', 'grad_norm': '0.04421', 'learning_rate': '2.703e-07', 'epoch': '2.966'}
{'eval_loss': '0.01462', 'eval_accuracy': '0.9979', 'eval_precision': '0.9978', 'eval_recall': '0.9957', 'eval_f1': '0.9968', 'eval_runtime': '6.671', 'eval_samples_per_second': '212.1', 'eval_steps_per_second': '6.745', 'epoch': '3'}
Writing model shards: 100%|█| 1/1 [00:01<00:00
{'train_runtime': '609.4', 'train_samples_per_second': '55.73', 'train_steps_per_second': '1.743', 'train_loss': '0.1068', 'epoch': '3'}
100%|█████| 1062/1062 [10:10<00:00,  1.74it/s]
Writing model shards: 100%|█| 1/1 [00:00<00:00
100%|█████████| 45/45 [00:06<00:00,  6.91it/s]

=== TEST RESULTS ===
{
  "model": "roberta-base",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 11320,
    "val": 1415,
    "test": 1415
  },
  "accuracy": 0.992226148409894,
  "precision": 0.9913419913419913,
  "recall": 0.9849462365591398,
  "f1": 0.9881337648327939,
  "false_positive_rate": 0.004210526315789474,
  "confusion": {
    "tn": 946,
    "fp": 4,
    "fn": 7,
    "tp": 458
  }
}

Accuracy by source:
  ceas_ham           n= 150  accuracy=1.000
  enron_ham          n= 300  accuracy=0.997
  ling_ham           n= 150  accuracy=1.000
  nazario            n= 151  accuracy=0.987
  nigerian           n= 314  accuracy=0.984
  spamassassin_ham   n= 200  accuracy=0.995
  trec_ham           n= 150  accuracy=0.987

Saved model to: D:\Phishy\backend\models\roberta-base