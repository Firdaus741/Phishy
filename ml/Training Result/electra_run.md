(.venv) PS D:\Phishy> python ml\train.py google/electra-small-discriminator

=== DATA CHECK ===
File: D:\Phishy\ml\data\unified\unified.csv
Sources in train: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']
train rows=11320  legit= 7600  phishing= 3720
val   rows= 1415  legit=  950  phishing=  465
test  rows= 1415  legit=  950  phishing=  465
Train/test overlap: none (checked)

Model: google/electra-small-discriminator | quick mode: False
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
config.json: 100%|██████████████████| 665/665 [00:00<00:00, 3.57MB/s]
D:\Phishy\.venv\Lib\site-packages\huggingface_hub\file_download.py:149: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in D:\cache\huggingface\hub\models--google--electra-small-discriminator. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabledby setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate DeveloperMode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)
tokenizer_config.json: 100%|███████| 48.0/48.0 [00:00<00:00, 291kB/s]
vocab.txt: 100%|██████████████████| 232k/232k [00:00<00:00, 4.78MB/s]
tokenizer.json: 100%|█████████████| 466k/466k [00:00<00:00, 10.9MB/s]
pytorch_model.bin: 100%|████████| 54.2M/54.2M [00:06<00:00, 8.47MB/s]
Loading weights: 100%|██████████| 199/199 [00:00<00:00, 27255.31it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.391', 'grad_norm': '3.221', 'learning_rate': '4.8e-06', 'epoch': '0.07062'}                                                    
model.safetensors: 100%|████████| 54.2M/54.2M [00:05<00:00, 9.26MB/s]
{'loss': '1.329', 'grad_norm': '1.81', 'learning_rate': '9.8e-06', 'epoch': '0.1412'}                                                      
{'loss': '1.214', 'grad_norm': '1.992', 'learning_rate': '1.48e-05', 'epoch': '0.2119'}                                                    
{'loss': '1.021', 'grad_norm': '2.946', 'learning_rate': '1.98e-05', 'epoch': '0.2825'}                                                    
{'loss': '0.8022', 'grad_norm': '2.21', 'learning_rate': '1.95e-05', 'epoch': '0.3531'}                                                    
{'loss': '0.5946', 'grad_norm': '2.575', 'learning_rate': '1.898e-05', 'epoch': '0.4237'}                                                  
{'loss': '0.4803', 'grad_norm': '17.79', 'learning_rate': '1.846e-05', 'epoch': '0.4944'}                                                  
{'loss': '0.3639', 'grad_norm': '8.32', 'learning_rate': '1.794e-05','epoch': '0.565'}                                                    
{'loss': '0.3008', 'grad_norm': '6.493', 'learning_rate': '1.742e-05', 'epoch': '0.6356'}                                                  
{'loss': '0.2522', 'grad_norm': '24.03', 'learning_rate': '1.69e-05','epoch': '0.7062'}                                                   
{'loss': '0.2462', 'grad_norm': '1.882', 'learning_rate': '1.638e-05', 'epoch': '0.7768'}                                                  
{'loss': '0.1975', 'grad_norm': '1.244', 'learning_rate': '1.586e-05', 'epoch': '0.8475'}                                                  
{'loss': '0.1714', 'grad_norm': '0.8404', 'learning_rate': '1.534e-05', 'epoch': '0.9181'}                                                 
{'loss': '0.1322', 'grad_norm': '1.231', 'learning_rate': '1.482e-05', 'epoch': '0.9887'}                                                  
{'eval_loss': '0.08216', 'eval_accuracy': '0.9802', 'eval_precision':'0.9581', 'eval_recall': '0.9828', 'eval_f1': '0.9703', 'eval_runtime': '1.653', 'eval_samples_per_second': '855.9', 'eval_steps_per_second': '27.22', 'epoch': '1'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00, 14.31it/s]
{'loss': '0.1182', 'grad_norm': '1.59', 'learning_rate': '1.43e-05', 'epoch': '1.059'}                                                     
{'loss': '0.1213', 'grad_norm': '15.07', 'learning_rate': '1.378e-05', 'epoch': '1.13'}                                                    
{'loss': '0.1144', 'grad_norm': '1.042', 'learning_rate': '1.326e-05', 'epoch': '1.201'}                                                   
{'loss': '0.1238', 'grad_norm': '0.7968', 'learning_rate': '1.274e-05', 'epoch': '1.271'}                                                  
{'loss': '0.08968', 'grad_norm': '0.4271', 'learning_rate': '1.222e-05', 'epoch': '1.342'}                                                 
{'loss': '0.1475', 'grad_norm': '1.589', 'learning_rate': '1.17e-05','epoch': '1.412'}                                                    
{'loss': '0.0851', 'grad_norm': '46.82', 'learning_rate': '1.119e-05', 'epoch': '1.483'}                                                   
{'loss': '0.1145', 'grad_norm': '31.32', 'learning_rate': '1.067e-05', 'epoch': '1.554'}                                                   
{'loss': '0.09564', 'grad_norm': '0.3374', 'learning_rate': '1.015e-05', 'epoch': '1.624'}                                                 
{'loss': '0.07275', 'grad_norm': '0.3318', 'learning_rate': '9.626e-06', 'epoch': '1.695'}                                                 
{'loss': '0.1062', 'grad_norm': '42.72', 'learning_rate': '9.106e-06', 'epoch': '1.766'}                                                   
{'loss': '0.1037', 'grad_norm': '0.2983', 'learning_rate': '8.586e-06', 'epoch': '1.836'}                                                  
{'loss': '0.07744', 'grad_norm': '0.2656', 'learning_rate': '8.067e-06', 'epoch': '1.907'}                                                 
{'loss': '0.09687', 'grad_norm': '1.331', 'learning_rate': '7.547e-06', 'epoch': '1.977'}                                                  
{'eval_loss': '0.04611', 'eval_accuracy': '0.9887', 'eval_precision':'0.987', 'eval_recall': '0.9785', 'eval_f1': '0.9827', 'eval_runtime': '1.629', 'eval_samples_per_second': '868.7', 'eval_steps_per_second': '27.63', 'epoch': '2'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00, 16.58it/s]
{'loss': '0.1094', 'grad_norm': '0.2232', 'learning_rate': '7.027e-06', 'epoch': '2.048'}                                                  
{'loss': '0.08515', 'grad_norm': '18.45', 'learning_rate': '6.507e-06', 'epoch': '2.119'}                                                  
{'loss': '0.03487', 'grad_norm': '0.2108', 'learning_rate': '5.988e-06', 'epoch': '2.189'}                                                 
{'loss': '0.05164', 'grad_norm': '3.696', 'learning_rate': '5.468e-06', 'epoch': '2.26'}                                                   
{'loss': '0.05214', 'grad_norm': '0.2081', 'learning_rate': '4.948e-06', 'epoch': '2.331'}                                                 
{'loss': '0.07176', 'grad_norm': '30.74', 'learning_rate': '4.428e-06', 'epoch': '2.401'}                                                  
{'loss': '0.04442', 'grad_norm': '0.2124', 'learning_rate': '3.909e-06', 'epoch': '2.472'}                                                 
{'loss': '0.1006', 'grad_norm': '0.2106', 'learning_rate': '3.389e-06', 'epoch': '2.542'}                                                  
{'loss': '0.07059', 'grad_norm': '30.28', 'learning_rate': '2.869e-06', 'epoch': '2.613'}                                                  
{'loss': '0.09', 'grad_norm': '0.1887', 'learning_rate': '2.349e-06','epoch': '2.684'}                                                    
{'loss': '0.04593', 'grad_norm': '0.1882', 'learning_rate': '1.83e-06', 'epoch': '2.754'}                                                  
{'loss': '0.08676', 'grad_norm': '0.1831', 'learning_rate': '1.31e-06', 'epoch': '2.825'}                                                  
{'loss': '0.09263', 'grad_norm': '0.1909', 'learning_rate': '7.9e-07', 'epoch': '2.895'}                                                   
{'loss': '0.0463', 'grad_norm': '0.1711', 'learning_rate': '2.703e-07', 'epoch': '2.966'}                                                  
{'eval_loss': '0.04093', 'eval_accuracy': '0.9915', 'eval_precision':'0.9935', 'eval_recall': '0.9806', 'eval_f1': '0.987', 'eval_runtime': '1.654', 'eval_samples_per_second': '855.5', 'eval_steps_per_second': '27.21', 'epoch': '3'}
Writing model shards: 100%|████████████| 1/1 [00:00<00:00, 20.00it/s]
{'train_runtime': '146.3', 'train_samples_per_second': '232.1', 'train_steps_per_second': '7.257', 'train_loss': '0.2579', 'epoch': '3'}   
100%|████████████████████████████| 1062/1062 [02:26<00:00,  7.25it/s]
Writing model shards: 100%|████████████| 1/1 [00:00<00:00,  1.78it/s]
100%|████████████████████████████████| 45/45 [00:01<00:00, 27.44it/s]

=== TEST RESULTS ===
{
  "model": "google/electra-small-discriminator",
  "data_file": "D:\\Phishy\\ml\\data\\unified\\unified.csv",
  "rows": {
    "train": 11320,
    "val": 1415,
    "test": 1415
  },
  "accuracy": 0.9886925795053003,
  "precision": 0.9891067538126361,
  "recall": 0.9763440860215054,
  "f1": 0.9826839826839827,
  "false_positive_rate": 0.005263157894736842,
  "confusion": {
    "tn": 945,
    "fp": 5,
    "fn": 11,
    "tp": 454
  }
}

Accuracy by source:
  ceas_ham           n= 150  accuracy=0.993
  enron_ham          n= 300  accuracy=0.990
  ling_ham           n= 150  accuracy=1.000
  nazario            n= 151  accuracy=0.960
  nigerian           n= 314  accuracy=0.984
  spamassassin_ham   n= 200  accuracy=1.000
  trec_ham           n= 150  accuracy=0.993

Saved model to: D:\Phishy\backend\models\electra-small-discriminator