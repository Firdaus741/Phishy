(.venv) PS D:\Phishy> python ml\train.py

=== DATA CHECK ===
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=11320  legit= 7600  phishing= 3720
val   rows= 1415  legit=  950  phishing=  465
test  rows= 1415  legit=  950  phishing=  465
Train/test overlap: none (checked)

Model: distilbert-base-uncased | quick mode: False
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 727.89it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_transform.bias    | UNEXPECTED | 
classifier.weight       | MISSING    | 
pre_classifier.bias     | MISSING    | 
pre_classifier.weight   | MISSING    | 
classifier.bias         | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.336', 'grad_norm': '3.029', 'learning_rate': '4.8e-06', 'epoch': '0.07062'}                                                            
{'loss': '1.101', 'grad_norm': '3.952', 'learning_rate': '9.8e-06', 'epoch': '0.1412'}                                                             
{'loss': '0.4456', 'grad_norm': '2.086', 'learning_rate': '1.48e-05', 'epoch': '0.2119'}                                                           
{'loss': '0.1961', 'grad_norm': '14.47', 'learning_rate': '1.98e-05', 'epoch': '0.2825'}                                                           
{'loss': '0.2407', 'grad_norm': '3.289', 'learning_rate': '1.95e-05', 'epoch': '0.3531'}                                                           
{'loss': '0.1027', 'grad_norm': '0.2014', 'learning_rate': '1.898e-05', 'epoch': '0.4237'}                                                         
{'loss': '0.1372', 'grad_norm': '9.498', 'learning_rate': '1.846e-05', 'epoch': '0.4944'}                                                          
{'loss': '0.04117', 'grad_norm': '10.35', 'learning_rate': '1.794e-05', 'epoch': '0.565'}                                                          
{'loss': '0.1352', 'grad_norm': '5.313', 'learning_rate': '1.742e-05', 'epoch': '0.6356'}                                                          
{'loss': '0.05198', 'grad_norm': '0.6321', 'learning_rate': '1.69e-05', 'epoch': '0.7062'}                                                         
{'loss': '0.1173', 'grad_norm': '0.5314', 'learning_rate': '1.638e-05', 'epoch': '0.7768'}                                                         
{'loss': '0.06658', 'grad_norm': '0.05747', 'learning_rate': '1.586e-05', 'epoch': '0.8475'}                                                       
{'loss': '0.04741', 'grad_norm': '0.07102', 'learning_rate': '1.534e-05', 'epoch': '0.9181'}                                                       
{'loss': '0.06813', 'grad_norm': '17.79', 'learning_rate': '1.482e-05', 'epoch': '0.9887'}                                                         
{'eval_loss': '0.02962', 'eval_accuracy': '0.9915', 'eval_precision': '0.9935', 'eval_recall': '0.9806', 'eval_f1': '0.987', 'eval_runtime': '3.393', 'eval_samples_per_second': '417', 'eval_steps_per_second': '13.26', 'epoch': '1'}                                                                
Writing model shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.21s/it]
{'loss': '0.0388', 'grad_norm': '0.05267', 'learning_rate': '1.43e-05', 'epoch': '1.059'}                                                          
{'loss': '0.02519', 'grad_norm': '0.2156', 'learning_rate': '1.378e-05', 'epoch': '1.13'}                                                          
{'loss': '0.06802', 'grad_norm': '0.03448', 'learning_rate': '1.326e-05', 'epoch': '1.201'}                                                        
{'loss': '0.05129', 'grad_norm': '0.05133', 'learning_rate': '1.274e-05', 'epoch': '1.271'}                                                        
{'loss': '0.03604', 'grad_norm': '0.9815', 'learning_rate': '1.222e-05', 'epoch': '1.342'}                                                         
{'loss': '0.03406', 'grad_norm': '11.51', 'learning_rate': '1.17e-05', 'epoch': '1.412'}                                                           
{'loss': '0.01498', 'grad_norm': '0.1218', 'learning_rate': '1.119e-05', 'epoch': '1.483'}                                                         
{'loss': '0.03412', 'grad_norm': '1.906', 'learning_rate': '1.067e-05', 'epoch': '1.554'}                                                          
{'loss': '0.01717', 'grad_norm': '0.04904', 'learning_rate': '1.015e-05', 'epoch': '1.624'}                                                        
{'loss': '0.04087', 'grad_norm': '0.03252', 'learning_rate': '9.626e-06', 'epoch': '1.695'}                                                        
{'loss': '0.04005', 'grad_norm': '0.04072', 'learning_rate': '9.106e-06', 'epoch': '1.766'}                                                        
{'loss': '0.05239', 'grad_norm': '0.06804', 'learning_rate': '8.586e-06', 'epoch': '1.836'}                                                        
{'loss': '0.02161', 'grad_norm': '0.02026', 'learning_rate': '8.067e-06', 'epoch': '1.907'}                                                        
{'loss': '0.07225', 'grad_norm': '10.3', 'learning_rate': '7.547e-06', 'epoch': '1.977'}                                                           
{'eval_loss': '0.01864', 'eval_accuracy': '0.9958', 'eval_precision': '0.9935', 'eval_recall': '0.9935', 'eval_f1': '0.9935', 'eval_runtime': '3.352', 'eval_samples_per_second': '422.1', 'eval_steps_per_second': '13.42', 'epoch': '2'}                                                             
Writing model shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.43it/s]
{'loss': '0.02716', 'grad_norm': '0.02721', 'learning_rate': '7.027e-06', 'epoch': '2.048'}                                                        
{'loss': '0.01484', 'grad_norm': '16.9', 'learning_rate': '6.507e-06', 'epoch': '2.119'}                                                           
{'loss': '0.01884', 'grad_norm': '0.01963', 'learning_rate': '5.988e-06', 'epoch': '2.189'}                                                        
{'loss': '0.003313', 'grad_norm': '0.03287', 'learning_rate': '5.468e-06', 'epoch': '2.26'}                                                        
{'loss': '0.008844', 'grad_norm': '0.02138', 'learning_rate': '4.948e-06', 'epoch': '2.331'}                                                       
{'loss': '0.0012', 'grad_norm': '0.01863', 'learning_rate': '4.428e-06', 'epoch': '2.401'}                                                         
{'loss': '0.001197', 'grad_norm': '0.01887', 'learning_rate': '3.909e-06', 'epoch': '2.472'}                                                       
{'loss': '0.02034', 'grad_norm': '0.02298', 'learning_rate': '3.389e-06', 'epoch': '2.542'}                                                        
{'loss': '0.02306', 'grad_norm': '0.1696', 'learning_rate': '2.869e-06', 'epoch': '2.613'}                                                         
{'loss': '0.01821', 'grad_norm': '0.02007', 'learning_rate': '2.349e-06', 'epoch': '2.684'}                                                        
{'loss': '0.02559', 'grad_norm': '0.01684', 'learning_rate': '1.83e-06', 'epoch': '2.754'}                                                         
{'loss': '0.000927', 'grad_norm': '0.01803', 'learning_rate': '1.31e-06', 'epoch': '2.825'}                                                        
{'loss': '0.03903', 'grad_norm': '0.012', 'learning_rate': '7.9e-07', 'epoch': '2.895'}                                                            
{'loss': '0.01466', 'grad_norm': '0.0262', 'learning_rate': '2.703e-07', 'epoch': '2.966'}                                                         
{'eval_loss': '0.02595', 'eval_accuracy': '0.9943', 'eval_precision': '0.9914', 'eval_recall': '0.9914', 'eval_f1': '0.9914', 'eval_runtime': '3.302', 'eval_samples_per_second': '428.5', 'eval_steps_per_second': '13.63', 'epoch': '3'}                                                             
Writing model shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.48it/s]
{'train_runtime': '306.4', 'train_samples_per_second': '110.8', 'train_steps_per_second': '3.466', 'train_loss': '0.1142', 'epoch': '3'}           
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 1062/1062 [05:06<00:00,  3.46it/s]
Writing model shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.71s/it]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 45/45 [00:03<00:00, 13.62it/s]

=== TEST RESULTS ===
{
  "model": "distilbert-base-uncased",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 11320,
    "val": 1415,
    "test": 1415
  },
  "accuracy": 0.9936395759717315,
  "precision": 0.9978165938864629,
  "recall": 0.9827956989247312,
  "f1": 0.9902491874322861,
  "false_positive_rate": 0.0010526315789473684,
  "confusion": {
    "tn": 949,
    "fp": 1,
    "fn": 8,
    "tp": 457
  }
}

Accuracy by source:
  ceas_ham           n= 150  accuracy=1.000
  enron_ham          n= 300  accuracy=0.997
  ling_ham           n= 150  accuracy=1.000
  nazario            n= 151  accuracy=0.967
  nigerian           n= 314  accuracy=0.990
  spamassassin_ham   n= 200  accuracy=1.000
  trec_ham           n= 150  accuracy=1.000

Saved model to: D:\Phishy\backend\models\distilbert-base-uncased