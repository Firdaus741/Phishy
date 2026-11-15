D:\Phishy> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\Phishy\.venv\Scripts\Activate.ps1)
(.venv) PS D:\Phishy> python ml\benchmark.py loso --model distilbert-base-uncased
Data: D:\Phishy\ml\data\unified\unified.csv
sources: ['ceas_ham', 'enron_ham', 'ling_ham', 'nazario', 'nigerian', 'spamassassin_ham', 'trec_ham']

  [tfidf_logreg] held out ceas_ham           n= 1500  unseen=0.983
  [tfidf_logreg] held out enron_ham          n= 3000  unseen=0.997
  [tfidf_logreg] held out ling_ham           n= 1500  unseen=0.989
  [tfidf_logreg] held out nazario            n= 1510  unseen=0.037
  [tfidf_logreg] held out nigerian           n= 3140  unseen=0.005
  [tfidf_logreg] held out spamassassin_ham   n= 2000  unseen=0.998
  [tfidf_logreg] held out trec_ham           n= 1500  unseen=0.993

=== Leave-one-source-out: tfidf_logreg ===
        held_out          measures    n  unseen_acc  normal_acc  seconds   drop
        ceas_ham legit specificity 1500      0.9833      1.0000        7 0.0167
       enron_ham legit specificity 3000      0.9967      0.9967        6 0.0000
        ling_ham legit specificity 1500      0.9893      1.0000        6 0.0107
         nazario   phishing recall 1510      0.0371      0.9536        6 0.9165
        nigerian   phishing recall 3140      0.0054      0.9873        6 0.9819
spamassassin_ham legit specificity 2000      0.9975      1.0000        6 0.0025
        trec_ham legit specificity 1500      0.9933      0.9933        7 0.0000
(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)

Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 774.54it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.7764', 'grad_norm': '0.612', 'learning_rate': '1.98e-05', 'epoch': '0.316'}        
{'loss': '0.123', 'grad_norm': '0.4545', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}      
{'loss': '0.08664', 'grad_norm': '8.379', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}     
{'loss': '0.05089', 'grad_norm': '0.1595', 'learning_rate': '8.801e-06', 'epoch': '1.262'}     
{'loss': '0.03649', 'grad_norm': '0.1042', 'learning_rate': '5.056e-06', 'epoch': '1.578'}     
{'loss': '0.0363', 'grad_norm': '0.04962', 'learning_rate': '1.311e-06', 'epoch': '1.894'}     
{'train_runtime': '183.3', 'train_samples_per_second': '110.4', 'train_steps_per_second': '3.458', 'train_loss': '0.177', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [03:03<00:00,  3.46it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:03<00:00, 13.11it/s]
  [distilbert-base-uncased] held out ceas_ham           n= 1500  unseen=0.983
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 519.51it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.7555', 'grad_norm': '5.104', 'learning_rate': '1.98e-05', 'epoch': '0.3584'}       
{'loss': '0.1279', 'grad_norm': '2.086', 'learning_rate': '1.568e-05', 'epoch': '0.7168'}      
{'loss': '0.07622', 'grad_norm': '10.28', 'learning_rate': '1.131e-05', 'epoch': '1.075'}      
{'loss': '0.03879', 'grad_norm': '0.06709', 'learning_rate': '6.943e-06', 'epoch': '1.434'}    
{'loss': '0.04832', 'grad_norm': '0.06941', 'learning_rate': '2.576e-06', 'epoch': '1.792'}    
{'train_runtime': '162.3', 'train_samples_per_second': '109.9', 'train_steps_per_second': '3.438', 'train_loss': '0.1918', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 558/558 [02:42<00:00,  3.44it/s]
100%|██████████████████████████████████████████████████████████| 94/94 [00:07<00:00, 12.03it/s]
  [distilbert-base-uncased] held out enron_ham          n= 3000  unseen=0.989
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 488.03it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.7694', 'grad_norm': '11.53', 'learning_rate': '1.98e-05', 'epoch': '0.316'}        
{'loss': '0.1298', 'grad_norm': '3.61', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}       
{'loss': '0.09387', 'grad_norm': '8.619', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}     
{'loss': '0.05218', 'grad_norm': '0.05986', 'learning_rate': '8.801e-06', 'epoch': '1.262'}    
{'loss': '0.04276', 'grad_norm': '0.06783', 'learning_rate': '5.056e-06', 'epoch': '1.578'}    
{'loss': '0.04175', 'grad_norm': '2.374', 'learning_rate': '1.311e-06', 'epoch': '1.894'}      
{'train_runtime': '187.8', 'train_samples_per_second': '107.8', 'train_steps_per_second': '3.376', 'train_loss': '0.1801', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [03:07<00:00,  3.38it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:03<00:00, 12.72it/s]
  [distilbert-base-uncased] held out ling_ham           n= 1500  unseen=0.983
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 525.88it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.6725', 'grad_norm': '0.2239', 'learning_rate': '1.98e-05', 'epoch': '0.3165'}      
{'loss': '0.07696', 'grad_norm': '0.1175', 'learning_rate': '1.628e-05', 'epoch': '0.6329'}    
{'loss': '0.04563', 'grad_norm': '0.06008', 'learning_rate': '1.252e-05', 'epoch': '0.9494'}   
{'loss': '0.03622', 'grad_norm': '0.401', 'learning_rate': '8.759e-06', 'epoch': '1.266'}      
{'loss': '0.02405', 'grad_norm': '1.4', 'learning_rate': '5e-06', 'epoch': '1.582'}            
{'loss': '0.01614', 'grad_norm': '0.02575', 'learning_rate': '1.241e-06', 'epoch': '1.899'}    
{'train_runtime': '187.5', 'train_samples_per_second': '107.8', 'train_steps_per_second': '3.37', 'train_loss': '0.1387', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 632/632 [03:07<00:00,  3.37it/s]
100%|██████████████████████████████████████████████████████████| 48/48 [00:03<00:00, 12.88it/s]
  [distilbert-base-uncased] held out nazario            n= 1510  unseen=0.300
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 590.32it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.6597', 'grad_norm': '8.255', 'learning_rate': '1.98e-05', 'epoch': '0.363'}        
{'loss': '0.06553', 'grad_norm': '0.1099', 'learning_rate': '1.562e-05', 'epoch': '0.726'}     
{'loss': '0.05329', 'grad_norm': '0.03403', 'learning_rate': '1.119e-05', 'epoch': '1.087'}    
{'loss': '0.0207', 'grad_norm': '0.03372', 'learning_rate': '6.77e-06', 'epoch': '1.45'}       
{'loss': '0.02612', 'grad_norm': '0.2596', 'learning_rate': '2.345e-06', 'epoch': '1.813'}     
{'train_runtime': '160.4', 'train_samples_per_second': '109.8', 'train_steps_per_second': '3.441', 'train_loss': '0.1538', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 552/552 [02:40<00:00,  3.44it/s]
100%|██████████████████████████████████████████████████████████| 99/99 [00:07<00:00, 12.50it/s]
  [distilbert-base-uncased] held out nigerian           n= 3140  unseen=0.079
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 479.92it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.7738', 'grad_norm': '1.313', 'learning_rate': '1.98e-05', 'epoch': '0.3289'}       
{'loss': '0.1156', 'grad_norm': '0.1632', 'learning_rate': '1.61e-05', 'epoch': '0.6579'}      
{'loss': '0.08635', 'grad_norm': '29.31', 'learning_rate': '1.217e-05', 'epoch': '0.9868'}     
{'loss': '0.04819', 'grad_norm': '23.85', 'learning_rate': '8.228e-06', 'epoch': '1.316'}      
{'loss': '0.05629', 'grad_norm': '0.1282', 'learning_rate': '4.291e-06', 'epoch': '1.645'}     
{'loss': '0.03783', 'grad_norm': '0.1589', 'learning_rate': '3.543e-07', 'epoch': '1.974'}     
{'train_runtime': '182.6', 'train_samples_per_second': '106.4', 'train_steps_per_second': '3.329', 'train_loss': '0.1849', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 608/608 [03:02<00:00,  3.33it/s]
100%|██████████████████████████████████████████████████████████| 63/63 [00:05<00:00, 12.04it/s]
  [distilbert-base-uncased] held out spamassassin_ham   n= 2000  unseen=0.997
Loading weights: 100%|██████████████████████████████████████| 100/100 [00:00<00:00, 434.67it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | 
------------------------+------------+-
vocab_transform.bias    | UNEXPECTED | 
vocab_layer_norm.bias   | UNEXPECTED | 
vocab_transform.weight  | UNEXPECTED | 
vocab_projector.bias    | UNEXPECTED | 
vocab_layer_norm.weight | UNEXPECTED | 
classifier.bias         | MISSING    | 
classifier.weight       | MISSING    | 
pre_classifier.weight   | MISSING    | 
pre_classifier.bias     | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.7489', 'grad_norm': '0.6533', 'learning_rate': '1.98e-05', 'epoch': '0.316'}       
{'loss': '0.1025', 'grad_norm': '0.1155', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}     
{'loss': '0.05985', 'grad_norm': '0.5641', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}    
{'loss': '0.054', 'grad_norm': '0.09358', 'learning_rate': '8.801e-06', 'epoch': '1.262'}      
{'loss': '0.03295', 'grad_norm': '0.0442', 'learning_rate': '5.056e-06', 'epoch': '1.578'}     
{'loss': '0.0407', 'grad_norm': '0.03503', 'learning_rate': '1.311e-06', 'epoch': '1.894'}     
{'train_runtime': '186', 'train_samples_per_second': '108.8', 'train_steps_per_second': '3.408', 'train_loss': '0.1649', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [03:06<00:00,  3.41it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:03<00:00, 12.83it/s]
  [distilbert-base-uncased] held out trec_ham           n= 1500  unseen=0.987

=== Leave-one-source-out: distilbert-base-uncased ===
        held_out          measures    n  unseen_acc  normal_acc  seconds   drop
        ceas_ham legit specificity 1500      0.9833      1.0000      195 0.0167
       enron_ham legit specificity 3000      0.9890      0.9967      176 0.0077
        ling_ham legit specificity 1500      0.9833      1.0000      198 0.0167
         nazario   phishing recall 1510      0.3000      0.9669      197 0.6669
        nigerian   phishing recall 3140      0.0790      0.9904      174 0.9114
spamassassin_ham legit specificity 2000      0.9965      1.0000      195 0.0035
        trec_ham legit specificity 1500      0.9873      1.0000      196 0.0127
(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)
