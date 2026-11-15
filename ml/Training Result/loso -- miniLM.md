(.venv) PS D:\Phishy> python ml\benchmark.py loso --model microsoft/MiniLM-L12-H384-uncased
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
        ceas_ham legit specificity 1500      0.9833      1.0000        8 0.0167
       enron_ham legit specificity 3000      0.9967      0.9967        7 0.0000
        ling_ham legit specificity 1500      0.9893      1.0000        8 0.0107
         nazario   phishing recall 1510      0.0371      0.9536        8 0.9165
        nigerian   phishing recall 3140      0.0054      0.9873        8 0.9819
spamassassin_ham legit specificity 2000      0.9975      1.0000        7 0.0025
        trec_ham legit specificity 1500      0.9933      0.9933        6 0.0000
(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)

Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 20902.72it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
{'loss': '1.04', 'grad_norm': 'inf', 'learning_rate': '1.98e-05', 'epoch': '0.316'}            
{'loss': '0.2232', 'grad_norm': '0.4225', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}     
{'loss': '0.1455', 'grad_norm': '0.4143', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}     
{'loss': '0.0968', 'grad_norm': '15.05', 'learning_rate': '8.801e-06', 'epoch': '1.262'}       
{'loss': '0.07136', 'grad_norm': '3.539', 'learning_rate': '5.056e-06', 'epoch': '1.578'}      
{'loss': '0.08231', 'grad_norm': '0.1402', 'learning_rate': '1.311e-06', 'epoch': '1.894'}     
{'train_runtime': '153.8', 'train_samples_per_second': '131.6', 'train_steps_per_second': '4.123', 'train_loss': '0.2652', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [02:33<00:00,  4.12it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:02<00:00, 16.21it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out ceas_ham           n= 1500  unseen=0.991
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 16095.54it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.035', 'grad_norm': '22.77', 'learning_rate': '1.98e-05', 'epoch': '0.3584'}        
{'loss': '0.231', 'grad_norm': '0.4694', 'learning_rate': '1.568e-05', 'epoch': '0.7168'}      
{'loss': '0.1437', 'grad_norm': '5.928', 'learning_rate': '1.131e-05', 'epoch': '1.075'}       
{'loss': '0.08512', 'grad_norm': '0.2736', 'learning_rate': '6.943e-06', 'epoch': '1.434'}     
{'loss': '0.07667', 'grad_norm': '0.1691', 'learning_rate': '2.576e-06', 'epoch': '1.792'}     
{'train_runtime': '136.2', 'train_samples_per_second': '131', 'train_steps_per_second': '4.097', 'train_loss': '0.2897', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 558/558 [02:16<00:00,  4.10it/s]
100%|██████████████████████████████████████████████████████████| 94/94 [00:06<00:00, 15.06it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out enron_ham          n= 3000  unseen=0.992
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 16185.74it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.052', 'grad_norm': '46.95', 'learning_rate': '1.98e-05', 'epoch': '0.316'}         
{'loss': '0.2488', 'grad_norm': '27.41', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}      
{'loss': '0.1782', 'grad_norm': '1.912', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}      
{'loss': '0.1174', 'grad_norm': '1.421', 'learning_rate': '8.801e-06', 'epoch': '1.262'}       
{'loss': '0.09595', 'grad_norm': '32.27', 'learning_rate': '5.056e-06', 'epoch': '1.578'}      
{'loss': '0.08962', 'grad_norm': '40.04', 'learning_rate': '1.311e-06', 'epoch': '1.894'}      
{'train_runtime': '152.3', 'train_samples_per_second': '132.9', 'train_steps_per_second': '4.162', 'train_loss': '0.2858', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [02:32<00:00,  4.16it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:02<00:00, 15.67it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out ling_ham           n= 1500  unseen=0.987
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 19530.76it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '0.9735', 'grad_norm': '1.359', 'learning_rate': '1.98e-05', 'epoch': '0.3165'}       
{'loss': '0.145', 'grad_norm': '0.3222', 'learning_rate': '1.628e-05', 'epoch': '0.6329'}      
{'loss': '0.09166', 'grad_norm': '0.1967', 'learning_rate': '1.252e-05', 'epoch': '0.9494'}    
{'loss': '0.08205', 'grad_norm': '0.1749', 'learning_rate': '8.759e-06', 'epoch': '1.266'}     
{'loss': '0.06582', 'grad_norm': '0.1607', 'learning_rate': '5e-06', 'epoch': '1.582'}         
{'loss': '0.04922', 'grad_norm': '0.1532', 'learning_rate': '1.241e-06', 'epoch': '1.899'}     
{'train_runtime': '155.5', 'train_samples_per_second': '130.1', 'train_steps_per_second': '4.065', 'train_loss': '0.2252', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 632/632 [02:35<00:00,  4.07it/s]
100%|██████████████████████████████████████████████████████████| 48/48 [00:02<00:00, 16.90it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out nazario            n= 1510  unseen=0.239
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 12729.59it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.006', 'grad_norm': '7.891', 'learning_rate': '1.98e-05', 'epoch': '0.363'}         
{'loss': '0.1944', 'grad_norm': '0.4048', 'learning_rate': '1.562e-05', 'epoch': '0.726'}      
{'loss': '0.08622', 'grad_norm': '0.3143', 'learning_rate': '1.119e-05', 'epoch': '1.087'}     
{'loss': '0.07254', 'grad_norm': '0.2562', 'learning_rate': '6.77e-06', 'epoch': '1.45'}       
{'loss': '0.08742', 'grad_norm': '0.2337', 'learning_rate': '2.345e-06', 'epoch': '1.813'}     
{'train_runtime': '131.5', 'train_samples_per_second': '134', 'train_steps_per_second': '4.199', 'train_loss': '0.2711', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 552/552 [02:11<00:00,  4.20it/s]
100%|██████████████████████████████████████████████████████████| 99/99 [00:06<00:00, 16.23it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out nigerian           n= 3140  unseen=0.091
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 17857.27it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.045', 'grad_norm': '1.949', 'learning_rate': '1.98e-05', 'epoch': '0.3289'}        
{'loss': '0.2263', 'grad_norm': '0.4419', 'learning_rate': '1.61e-05', 'epoch': '0.6579'}      
{'loss': '0.1774', 'grad_norm': '70.14', 'learning_rate': '1.217e-05', 'epoch': '0.9868'}      
{'loss': '0.1071', 'grad_norm': '46.84', 'learning_rate': '8.228e-06', 'epoch': '1.316'}       
{'loss': '0.1007', 'grad_norm': '4.305', 'learning_rate': '4.291e-06', 'epoch': '1.645'}       
{'loss': '0.08252', 'grad_norm': '23.59', 'learning_rate': '3.543e-07', 'epoch': '1.974'}      
{'train_runtime': '146.9', 'train_samples_per_second': '132.3', 'train_steps_per_second': '4.139', 'train_loss': '0.2862', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 608/608 [02:26<00:00,  4.14it/s]
100%|██████████████████████████████████████████████████████████| 63/63 [00:03<00:00, 16.11it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out spamassassin_ham   n= 2000  unseen=0.988
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 18325.39it/s]
[transformers] BertForSequenceClassification LOAD REPORT from: microsoft/MiniLM-L12-H384-uncased
Key               | Status  | 
------------------+---------+-
classifier.bias   | MISSING | 
classifier.weight | MISSING | 

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.03', 'grad_norm': '6.177', 'learning_rate': '1.98e-05', 'epoch': '0.316'}          
{'loss': '0.2122', 'grad_norm': '0.4191', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}     
{'loss': '0.1383', 'grad_norm': '81.46', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}      
{'loss': '0.09808', 'grad_norm': '0.2027', 'learning_rate': '8.801e-06', 'epoch': '1.262'}     
{'loss': '0.08482', 'grad_norm': '0.1618', 'learning_rate': '5.056e-06', 'epoch': '1.578'}     
{'loss': '0.06452', 'grad_norm': '0.1681', 'learning_rate': '1.311e-06', 'epoch': '1.894'}     
{'train_runtime': '153.2', 'train_samples_per_second': '132.1', 'train_steps_per_second': '4.139', 'train_loss': '0.2599', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [02:33<00:00,  4.14it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:02<00:00, 15.78it/s]
  [microsoft/MiniLM-L12-H384-uncased] held out trec_ham           n= 1500  unseen=0.975

=== Leave-one-source-out: microsoft/MiniLM-L12-H384-uncased ===
        held_out          measures    n  unseen_acc  normal_acc  seconds   drop
        ceas_ham legit specificity 1500      0.9913      1.0000      162 0.0087
       enron_ham legit specificity 3000      0.9917      0.9933      147 0.0016
        ling_ham legit specificity 1500      0.9867      1.0000      169 0.0133
         nazario   phishing recall 1510      0.2391      0.9735      163 0.7344
        nigerian   phishing recall 3140      0.0911      0.9904      143 0.8993
spamassassin_ham legit specificity 2000      0.9875      1.0000      155 0.0125
        trec_ham legit specificity 1500      0.9753      0.9933      160 0.0180
(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)