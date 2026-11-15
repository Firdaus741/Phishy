(.venv) PS D:\Phishy> python ml\train.py bert-base-uncased            
                                                                      
=== DATA CHECK ===                                                   
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=11320  legit= 7600  phishing= 3720
val   rows= 1415  legit=  950  phishing=  465
test  rows= 1415  legit=  950  phishing=  465
Train/test overlap: none (checked)

Model: bert-base-uncased | quick mode: False
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Loading weights: 100%|████████████| 199/199 [00:00<00:00, 515.60it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: bert-base-uncased
Key                                        | Status     | 
-------------------------------------------+------------+-
cls.predictions.transform.dense.bias       | UNEXPECTED | 
cls.predictions.bias                       | UNEXPECTED | 
cls.seq_relationship.bias                  | UNEXPECTED | 
cls.seq_relationship.weight                | UNEXPECTED | 
cls.predictions.transform.LayerNorm.bias   | UNEXPECTED | 
cls.predictions.transform.dense.weight     | UNEXPECTED | 
cls.predictions.transform.LayerNorm.weight | UNEXPECTED | 
classifier.weight                          | MISSING    | 
classifier.bias                            | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.363', 'grad_norm': '7.068', 'learning_rate': '4.8e-06', 'epoch': '0.07062'}
{'loss': '0.9494', 'grad_norm': '7.278', 'learning_rate': '9.8e-06', 'epoch': '0.1412'}
{'loss': '0.4669', 'grad_norm': '6.278', 'learning_rate': '1.48e-05','epoch': '0.2119'}
{'loss': '0.1878', 'grad_norm': '0.724', 'learning_rate': '1.98e-05','epoch': '0.2825'}
{'loss': '0.2199', 'grad_norm': '11.69', 'learning_rate': '1.95e-05','epoch': '0.3531'}
{'loss': '0.1158', 'grad_norm': '1.22', 'learning_rate': '1.898e-05','epoch': '0.4237'}
{'loss': '0.1168', 'grad_norm': '0.3645', 'learning_rate': '1.846e-05', 'epoch': '0.4944'}
{'loss': '0.03441', 'grad_norm': '41.69', 'learning_rate': '1.794e-05', 'epoch': '0.565'}
{'loss': '0.1179', 'grad_norm': '25.32', 'learning_rate': '1.742e-05', 'epoch': '0.6356'}
{'loss': '0.08176', 'grad_norm': '43.43', 'learning_rate': '1.69e-05', 'epoch': '0.7062'}
{'loss': '0.1424', 'grad_norm': '0.1194', 'learning_rate': '1.638e-05', 'epoch': '0.7768'}
{'loss': '0.04998', 'grad_norm': '0.0394', 'learning_rate': '1.586e-05', 'epoch': '0.8475'}
{'loss': '0.07368', 'grad_norm': '0.04251', 'learning_rate': '1.534e-05', 'epoch': '0.9181'}
{'loss': '0.06832', 'grad_norm': '0.156', 'learning_rate': '1.482e-05', 'epoch': '0.9887'}
{'eval_loss': '0.07177', 'eval_accuracy': '0.9823', 'eval_precision':'0.9977', 'eval_recall': '0.9484', 'eval_f1': '0.9724', 'eval_runtime': '8.072', 'eval_samples_per_second': '175.3', 'eval_steps_per_second': '5.574', 'epoch': '1'}
Writing model shards: 100%|████████████| 1/1 [00:01<00:00,  1.26s/it]
{'loss': '0.05985', 'grad_norm': '0.04713', 'learning_rate': '1.43e-05', 'epoch': '1.059'}
{'loss': '0.03583', 'grad_norm': '0.03172', 'learning_rate': '1.378e-05', 'epoch': '1.13'}
{'loss': '0.08602', 'grad_norm': '0.03852', 'learning_rate': '1.326e-05', 'epoch': '1.201'}
{'loss': '0.06133', 'grad_norm': '0.1505', 'learning_rate': '1.274e-05', 'epoch': '1.271'}
{'loss': '0.02736', 'grad_norm': '6.744', 'learning_rate': '1.222e-05', 'epoch': '1.342'}
{'loss': '0.02774', 'grad_norm': '0.03024', 'learning_rate': '1.17e-05', 'epoch': '1.412'}
{'loss': '0.02107', 'grad_norm': '0.06252', 'learning_rate': '1.119e-05', 'epoch': '1.483'}
{'loss': '0.03437', 'grad_norm': '0.05406', 'learning_rate': '1.067e-05', 'epoch': '1.554'}
{'loss': '0.01276', 'grad_norm': '0.02877', 'learning_rate': '1.015e-05', 'epoch': '1.624'}
{'loss': '0.05289', 'grad_norm': '0.0821', 'learning_rate': '9.626e-06', 'epoch': '1.695'}
{'loss': '0.03021', 'grad_norm': '0.02807', 'learning_rate': '9.106e-06', 'epoch': '1.766'}
{'loss': '0.03505', 'grad_norm': '0.02561', 'learning_rate': '8.586e-06', 'epoch': '1.836'}
{'loss': '0.03739', 'grad_norm': '0.02057', 'learning_rate': '8.067e-06', 'epoch': '1.907'}
{'loss': '0.05376', 'grad_norm': '0.2304', 'learning_rate': '7.547e-06', 'epoch': '1.977'}
{'eval_loss': '0.02377', 'eval_accuracy': '0.9943', 'eval_precision':'0.9914', 'eval_recall': '0.9914', 'eval_f1': '0.9914', 'eval_runtime': '7.351', 'eval_samples_per_second': '192.5', 'eval_steps_per_second': '6.122', 'epoch': '2'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  1.49it/s]
{'loss': '0.04207', 'grad_norm': '0.05274', 'learning_rate': '7.027e-06', 'epoch': '2.048'}
{'loss': '0.02148', 'grad_norm': '30.51', 'learning_rate': '6.507e-06', 'epoch': '2.119'}
{'loss': '0.0222', 'grad_norm': '0.01646', 'learning_rate': '5.988e-06', 'epoch': '2.189'}
{'loss': '0.0008792', 'grad_norm': '0.02126', 'learning_rate': '5.468e-06', 'epoch': '2.26'}
{'loss': '0.006565', 'grad_norm': '0.01739', 'learning_rate': '4.948e-06', 'epoch': '2.331'}
{'loss': '0.01747', 'grad_norm': '0.01607', 'learning_rate': '4.428e-06', 'epoch': '2.401'}
{'loss': '0.00108', 'grad_norm': '0.01649', 'learning_rate': '3.909e-06', 'epoch': '2.472'}
{'loss': '0.01448', 'grad_norm': '0.02263', 'learning_rate': '3.389e-06', 'epoch': '2.542'}
{'loss': '0.00246', 'grad_norm': '0.01461', 'learning_rate': '2.869e-06', 'epoch': '2.613'}
{'loss': '0.01869', 'grad_norm': '0.01084', 'learning_rate': '2.349e-06', 'epoch': '2.684'}
{'loss': '0.04038', 'grad_norm': '0.02887', 'learning_rate': '1.83e-06', 'epoch': '2.754'}
{'loss': '0.0004613', 'grad_norm': '0.01403', 'learning_rate': '1.31e-06', 'epoch': '2.825'}
{'loss': '0.02594', 'grad_norm': '0.009544', 'learning_rate': '7.9e-07', 'epoch': '2.895'}
{'loss': '0.003267', 'grad_norm': '0.02131', 'learning_rate': '2.703e-07', 'epoch': '2.966'}
{'eval_loss': '0.02456', 'eval_accuracy': '0.9951', 'eval_precision':'0.9935', 'eval_recall': '0.9914', 'eval_f1': '0.9925', 'eval_runtime': '6.597', 'eval_samples_per_second': '214.5', 'eval_steps_per_second': '6.821', 'epoch': '3'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  2.93it/s]
{'train_runtime': '640.9', 'train_samples_per_second': '52.98', 'train_steps_per_second': '1.657', 'train_loss': '0.1126', 'epoch': '3'}
100%|████████████████████████████| 1062/1062 [10:40<00:00,  1.97it/s][transformers] There were missing keys in the checkpoint model loaded:['bert.embeddings.LayerNorm.weight', 'bert.embeddings.LayerNorm.bias', 'bert.encoder.layer.0.attention.output.LayerNorm.weight', 'bert.encoder.layer.0.attention.output.LayerNorm.bias', 'bert.encoder.layer.0.output.LayerNorm.weight', 'bert.encoder.layer.0.output.LayerNorm.bias', 'bert.encoder.layer.1.attention.output.LayerNorm.weight', 'bert.encoder.layer.1.attention.output.LayerNorm.bias', 'bert.encoder.layer.1.output.LayerNorm.weight', 'bert.encoder.layer.1.output.LayerNorm.bias', 'bert.encoder.layer.2.attention.output.LayerNorm.weight', 'bert.encoder.layer.2.attention.output.LayerNorm.bias', 'bert.encoder.layer.2.output.LayerNorm.weight', 'bert.encoder.layer.2.output.LayerNorm.bias', 'bert.encoder.layer.3.attention.output.LayerNorm.weight', 'bert.encoder.layer.3.attention.output.LayerNorm.bias', 'bert.encoder.layer.3.output.LayerNorm.weight', 'bert.encoder.layer.3.output.LayerNorm.bias', 'bert.encoder.layer.4.attention.output.LayerNorm.weight', 'bert.encoder.layer.4.attention.output.LayerNorm.bias', 'bert.encoder.layer.4.output.LayerNorm.weight', 'bert.encoder.layer.4.output.LayerNorm.bias', 'bert.encoder.layer.5.attention.output.LayerNorm.weight', 'bert.encoder.layer.5.attention.output.LayerNorm.bias', 'bert.encoder.layer.5.output.LayerNorm.weight', 'bert.encoder.layer.5.output.LayerNorm.bias', 'bert.encoder.layer.6.attention.output.LayerNorm.weight', 'bert.encoder.layer.6.attention.output.LayerNorm.bias', 'bert.encoder.layer.6.output.LayerNorm.weight', 'bert.encoder.layer.6.output.LayerNorm.bias', 'bert.encoder.layer.7.attention.output.LayerNorm.weight', 'bert.encoder.layer.7.attention.output.LayerNorm.bias', 'bert.encoder.layer.7.output.LayerNorm.weight', 'bert.encoder.layer.7.output.LayerNorm.bias', 'bert.encoder.layer.8.attention.output.LayerNorm.weight', 'bert.encoder.layer.8.attention.output.LayerNorm.bias', 'bert.encoder.layer.8.output.LayerNorm.weight', 'bert.encoder.layer.8.output.LayerNorm.bias', 'bert.encoder.layer.9.attention.output.LayerNorm.weight', 'bert.encoder.layer.9.attention.output.LayerNorm.bias', 'bert.encoder.layer.9.output.LayerNorm.weight', 'bert.encoder.layer.9.output.LayerNorm.bias', 'bert.encoder.layer.10.attention.output.LayerNorm.weight', 'bert.encoder.layer.10.attention.output.LayerNorm.bias', 'bert.encoder.layer.10.output.LayerNorm.weight', 'bert.encoder.layer.10.output.LayerNorm.bias', 'bert.encoder.layer.11.attention.output.LayerNorm.weight', 'bert.encoder.layer.11.attention.output.LayerNorm.bias', 'bert.encoder.layer.11.output.LayerNorm.weight', 'bert.encoder.layer.11.output.LayerNorm.bias'].
[transformers] There were unexpected keys in the checkpoint model loaded: ['bert.embeddings.LayerNorm.beta', 'bert.embeddings.LayerNorm.gamma', 'bert.encoder.layer.0.attention.output.LayerNorm.beta', 'bert.encoder.layer.0.attention.output.LayerNorm.gamma', 'bert.encoder.layer.0.output.LayerNorm.beta', 'bert.encoder.layer.0.output.LayerNorm.gamma','bert.encoder.layer.1.attention.output.LayerNorm.beta', 'bert.encoder.layer.1.attention.output.LayerNorm.gamma', 'bert.encoder.layer.1.output.LayerNorm.beta', 'bert.encoder.layer.1.output.LayerNorm.gamma', 'bert.encoder.layer.2.attention.output.LayerNorm.beta', 'bert.encoder.layer.2.attention.output.LayerNorm.gamma', 'bert.encoder.layer.2.output.LayerNorm.beta', 'bert.encoder.layer.2.output.LayerNorm.gamma', 'bert.encoder.layer.3.attention.output.LayerNorm.beta', 'bert.encoder.layer.3.attention.output.LayerNorm.gamma', 'bert.encoder.layer.3.output.LayerNorm.beta', 'bert.encoder.layer.3.output.LayerNorm.gamma', 'bert.encoder.layer.4.attention.output.LayerNorm.beta', 'bert.encoder.layer.4.attention.output.LayerNorm.gamma', 'bert.encoder.layer.4.output.LayerNorm.beta', 'bert.encoder.layer.4.output.LayerNorm.gamma', 'bert.encoder.layer.5.attention.output.LayerNorm.beta', 'bert.encoder.layer.5.attention.output.LayerNorm.gamma', 'bert.encoder.layer.5.output.LayerNorm.beta', 'bert.encoder.layer.5.output.LayerNorm.gamma', 'bert.encoder.layer.6.attention.output.LayerNorm.beta', 'bert.encoder.layer.6.attention.output.LayerNorm.gamma', 'bert.encoder.layer.6.output.LayerNorm.beta', 'bert.encoder.layer.6.output.LayerNorm.gamma', 'bert.encoder.layer.7.attention.output.LayerNorm.beta', 'bert.encoder.layer.7.attention.output.LayerNorm.gamma', 'bert.encoder.layer.7.output.LayerNorm.beta', 'bert.encoder.layer.7.output.LayerNorm.gamma', 'bert.encoder.layer.8.attention.output.LayerNorm.beta', 'bert.encoder.layer.8.attention.output.LayerNorm.gamma', 'bert.encoder.layer.8.output.LayerNorm.beta', 'bert.encoder.layer.8.output.LayerNorm.gamma', 'bert.encoder.layer.9.attention.output.LayerNorm.beta', 'bert.encoder.layer.9.attention.output.LayerNorm.gamma', 'bert.encoder.layer.9.output.LayerNorm.beta', 'bert.encoder.layer.9.output.LayerNorm.gamma', 'bert.encoder.layer.10.attention.output.LayerNorm.beta', 'bert.encoder.layer.10.attention.output.LayerNorm.gamma', 'bert.encoder.layer.10.output.LayerNorm.beta', 'bert.encoder.layer.10.output.LayerNorm.gamma', 'bert.encoder.layer.11.attention.output.LayerNorm.beta', 'bert.encoder.layer.11.attention.output.LayerNorm.gamma', 'bert.encoder.layer.11.output.LayerNorm.beta', 'bert.encoder.layer.11.output.LayerNorm.gamma'].
100%|████████████████████████████| 1062/1062 [10:41<00:00,  1.66it/s]
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  2.82it/s]
100%|████████████████████████████████| 45/45 [00:06<00:00,  6.94it/s]

=== TEST RESULTS ===
{
  "model": "bert-base-uncased",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 11320,
    "val": 1415,
    "test": 1415
  },
  "accuracy": 0.9929328621908127,
  "precision": 0.9978118161925602,
  "recall": 0.9806451612903225,
  "f1": 0.9891540130151844,
  "false_positive_rate": 0.0010526315789473684,
  "confusion": {
    "tn": 949,
    "fp": 1,
    "fn": 9,
    "tp": 456
  }
}

Accuracy by source:
  ceas_ham           n= 150  accuracy=1.000
  enron_ham          n= 300  accuracy=0.997
  ling_ham           n= 150  accuracy=1.000
  nazario            n= 151  accuracy=0.967
  nigerian           n= 314  accuracy=0.987
  spamassassin_ham   n= 200  accuracy=1.000
  trec_ham           n= 150  accuracy=1.000

Saved model to: D:\Phishy\backend\models\bert-base-uncased