(.venv) PS D:\Phishy> python ml\train.py microsoft/MiniLM-L12-H384-uncased

=== DATA CHECK ===
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=11320  legit= 7600  phishing= 3720
val   rows= 1415  legit=  950  phishing=  465
test  rows= 1415  legit=  950  phishing=  465
Train/test overlap: none (checked)

Model: microsoft/MiniLM-L12-H384-uncased | quick mode: False
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
config.json: 100%|██████████████████| 385/385 [00:00<00:00, 2.14MB/s]
D:\Phishy\.venv\Lib\site-packages\huggingface_hub\file_download.py:149: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in D:\cache\huggingface\hub\models--microsoft--MiniLM-L12-H384-uncased. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable.For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate DeveloperMode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)
tokenizer_config.json: 100%|██████| 2.00/2.00 [00:00<00:00, 12.7kB/s]
vocab.txt: 100%|██████████████████| 232k/232k [00:00<00:00, 3.21MB/s]
special_tokens_map.json: 100%|███████| 112/112 [00:00<00:00, 635kB/s]
pytorch_model.bin: 100%|██████████| 133M/133M [00:16<00:00, 8.23MB/s]
Loading weights: 100%|██████████| 199/199 [00:00<00:00, 19159.99it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.386', 'grad_norm': '2.114', 'learning_rate': '4.8e-06', 'epoch': '0.07062'}                                                    
{'loss': '1.341', 'grad_norm': '1.106', 'learning_rate': '9.8e-06', 'epoch': '0.1412'}                                                     
{'loss': '0.9699', 'grad_norm': '5.793', 'learning_rate': '1.48e-05','epoch': '0.2119'}                                                   
model.safetensors: 100%|██████████| 133M/133M [00:21<00:00, 6.34MB/s]
{'loss': '0.4529', 'grad_norm': '1.746', 'learning_rate': '1.98e-05','epoch': '0.2825'}                                                   
{'loss': '0.2918', 'grad_norm': '1.116', 'learning_rate': '1.95e-05','epoch': '0.3531'}                                                   
{'loss': '0.2754', 'grad_norm': '0.7143', 'learning_rate': '1.898e-05', 'epoch': '0.4237'}                                                 
{'loss': '0.2211', 'grad_norm': '0.8911', 'learning_rate': '1.846e-05', 'epoch': '0.4944'}                                                 
{'loss': '0.1283', 'grad_norm': '85.16', 'learning_rate': '1.794e-05', 'epoch': '0.565'}                                                   
{'loss': '0.1403', 'grad_norm': '64.71', 'learning_rate': '1.742e-05', 'epoch': '0.6356'}                                                  
{'loss': '0.1277', 'grad_norm': '0.905', 'learning_rate': '1.69e-05','epoch': '0.7062'}                                                   
{'loss': '0.1476', 'grad_norm': '0.2804', 'learning_rate': '1.638e-05', 'epoch': '0.7768'}                                                 
{'loss': '0.1362', 'grad_norm': '27.29', 'learning_rate': '1.586e-05', 'epoch': '0.8475'}                                                  
{'loss': '0.1359', 'grad_norm': '28.17', 'learning_rate': '1.534e-05', 'epoch': '0.9181'}                                                  
{'loss': '0.1253', 'grad_norm': '67.47', 'learning_rate': '1.482e-05', 'epoch': '0.9887'}                                                  
{'eval_loss': '0.05415', 'eval_accuracy': '0.9845', 'eval_precision':'0.9826', 'eval_recall': '0.9699', 'eval_f1': '0.9762', 'eval_runtime': '2.674', 'eval_samples_per_second': '529.2', 'eval_steps_per_second': '16.83', 'epoch': '1'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  6.76it/s]
{'loss': '0.09451', 'grad_norm': '5.405', 'learning_rate': '1.43e-05', 'epoch': '1.059'}                                                   
{'loss': '0.08235', 'grad_norm': '0.777', 'learning_rate': '1.378e-05', 'epoch': '1.13'}                                                   
{'loss': '0.1178', 'grad_norm': '51.99', 'learning_rate': '1.326e-05', 'epoch': '1.201'}                                                   
{'loss': '0.1011', 'grad_norm': '0.1656', 'learning_rate': '1.274e-05', 'epoch': '1.271'}                                                  
{'loss': '0.08355', 'grad_norm': '15.56', 'learning_rate': '1.222e-05', 'epoch': '1.342'}                                                  
{'loss': '0.1085', 'grad_norm': '0.4308', 'learning_rate': '1.17e-05', 'epoch': '1.412'}                                                   
{'loss': '0.05484', 'grad_norm': '0.1482', 'learning_rate': '1.119e-05', 'epoch': '1.483'}                                                 
{'loss': '0.1077', 'grad_norm': '0.1485', 'learning_rate': '1.067e-05', 'epoch': '1.554'}                                                  
{'loss': '0.03862', 'grad_norm': '0.5953', 'learning_rate': '1.015e-05', 'epoch': '1.624'}                                                 
{'loss': '0.05211', 'grad_norm': '0.1418', 'learning_rate': '9.626e-06', 'epoch': '1.695'}                                                 
{'loss': '0.1061', 'grad_norm': '0.1224', 'learning_rate': '9.106e-06', 'epoch': '1.766'}                                                  
{'loss': '0.08684', 'grad_norm': '0.1323', 'learning_rate': '8.586e-06', 'epoch': '1.836'}                                                 
{'loss': '0.06931', 'grad_norm': '0.3189', 'learning_rate': '8.067e-06', 'epoch': '1.907'}                                                 
{'loss': '0.04593', 'grad_norm': '2.594', 'learning_rate': '7.547e-06', 'epoch': '1.977'}                                                  
{'eval_loss': '0.03586', 'eval_accuracy': '0.9915', 'eval_precision':'0.9768', 'eval_recall': '0.9978', 'eval_f1': '0.9872', 'eval_runtime': '2.767', 'eval_samples_per_second': '511.3', 'eval_steps_per_second': '16.26', 'epoch': '2'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  7.46it/s]
{'loss': '0.08053', 'grad_norm': '0.1149', 'learning_rate': '7.027e-06', 'epoch': '2.048'}                                                 
{'loss': '0.05222', 'grad_norm': '56.6', 'learning_rate': '6.507e-06', 'epoch': '2.119'}                                                   
{'loss': '0.02231', 'grad_norm': '0.09983', 'learning_rate': '5.988e-06', 'epoch': '2.189'}                                                
{'loss': '0.02937', 'grad_norm': '0.9094', 'learning_rate': '5.468e-06', 'epoch': '2.26'}                                                  
{'loss': '0.01403', 'grad_norm': '0.08917', 'learning_rate': '4.948e-06', 'epoch': '2.331'}                                                
{'loss': '0.0369', 'grad_norm': '81.15', 'learning_rate': '4.428e-06', 'epoch': '2.401'}                                                   
{'loss': '0.01912', 'grad_norm': '0.5773', 'learning_rate': '3.909e-06', 'epoch': '2.472'}                                                 
{'loss': '0.05844', 'grad_norm': '0.08237', 'learning_rate': '3.389e-06', 'epoch': '2.542'}                                                
{'loss': '0.07292', 'grad_norm': '15.48', 'learning_rate': '2.869e-06', 'epoch': '2.613'}                                                  
{'loss': '0.03289', 'grad_norm': '0.08209', 'learning_rate': '2.349e-06', 'epoch': '2.684'}                                                
{'loss': '0.05335', 'grad_norm': '0.0847', 'learning_rate': '1.83e-06', 'epoch': '2.754'}                                                  
{'loss': '0.06518', 'grad_norm': '0.08472', 'learning_rate': '1.31e-06', 'epoch': '2.825'}                                                 
{'loss': '0.1088', 'grad_norm': '0.08045', 'learning_rate': '7.9e-07', 'epoch': '2.895'}                                                   
{'loss': '0.02121', 'grad_norm': '0.08515', 'learning_rate': '2.703e-07', 'epoch': '2.966'}                                                
{'eval_loss': '0.02576', 'eval_accuracy': '0.9943', 'eval_precision':'0.9914', 'eval_recall': '0.9914', 'eval_f1': '0.9914', 'eval_runtime': '2.757', 'eval_samples_per_second': '513.3', 'eval_steps_per_second': '16.32', 'epoch': '3'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  5.36it/s]
{'train_runtime': '257.9', 'train_samples_per_second': '131.7', 'train_steps_per_second': '4.118', 'train_loss': '0.1818', 'epoch': '3'}   
100%|████████████████████████████| 1062/1062 [04:18<00:00,  4.12it/s]
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  7.12it/s]
100%|████████████████████████████████| 45/45 [00:02<00:00, 16.49it/s]

=== TEST RESULTS ===
{
  "model": "microsoft/MiniLM-L12-H384-uncased",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 11320,
    "val": 1415,
    "test": 1415
  },
  "accuracy": 0.9929328621908127,
  "precision": 0.9934924078091106,
  "recall": 0.9849462365591398,
  "f1": 0.9892008639308856,
  "false_positive_rate": 0.003157894736842105,
  "confusion": {
    "tn": 947,
    "fp": 3,
    "fn": 7,
    "tp": 458
  }
}

Accuracy by source:
  ceas_ham           n= 150  accuracy=1.000
  enron_ham          n= 300  accuracy=0.993
  ling_ham           n= 150  accuracy=1.000
  nazario            n= 151  accuracy=0.974
  nigerian           n= 314  accuracy=0.990
  spamassassin_ham   n= 200  accuracy=1.000
  trec_ham           n= 150  accuracy=0.993

Saved model to: D:\Phishy\backend\models\MiniLM-L12-H384-uncased