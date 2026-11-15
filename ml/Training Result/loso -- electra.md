PS D:\Phishy> python ml\benchmark.py loso --model google/electra-small-discriminator
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

Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 24216.40it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.254', 'grad_norm': '3.314', 'learning_rate': '1.98e-05', 'epoch': '0.316'}         
{'loss': '0.5548', 'grad_norm': '1.97', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}       
{'loss': '0.275', 'grad_norm': '1.54', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}        
{'loss': '0.1674', 'grad_norm': '0.87', 'learning_rate': '8.801e-06', 'epoch': '1.262'}        
{'loss': '0.1102', 'grad_norm': '3.754', 'learning_rate': '5.056e-06', 'epoch': '1.578'}       
{'loss': '0.1202', 'grad_norm': '0.53', 'learning_rate': '1.311e-06', 'epoch': '1.894'}        
{'train_runtime': '88.95', 'train_samples_per_second': '227.5', 'train_steps_per_second': '7.128', 'train_loss': '0.3973', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [01:28<00:00,  7.13it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:01<00:00, 25.59it/s]
  [google/electra-small-discriminator] held out ceas_ham           n= 1500  unseen=0.979
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 12736.39it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.269', 'grad_norm': '3.233', 'learning_rate': '1.98e-05', 'epoch': '0.3584'}        
{'loss': '0.5721', 'grad_norm': '1.498', 'learning_rate': '1.568e-05', 'epoch': '0.7168'}      
{'loss': '0.2883', 'grad_norm': '3.188', 'learning_rate': '1.131e-05', 'epoch': '1.075'}       
{'loss': '0.1906', 'grad_norm': '1.864', 'learning_rate': '6.943e-06', 'epoch': '1.434'}       
{'loss': '0.1535', 'grad_norm': '0.714', 'learning_rate': '2.576e-06', 'epoch': '1.792'}       
{'train_runtime': '78.51', 'train_samples_per_second': '227.2', 'train_steps_per_second': '7.108', 'train_loss': '0.4569', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 558/558 [01:18<00:00,  7.11it/s]
100%|██████████████████████████████████████████████████████████| 94/94 [00:03<00:00, 25.54it/s]
  [google/electra-small-discriminator] held out enron_ham          n= 3000  unseen=0.984
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 15431.35it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.252', 'grad_norm': '2.534', 'learning_rate': '1.98e-05', 'epoch': '0.316'}         
{'loss': '0.5732', 'grad_norm': '10.79', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}      
{'loss': '0.294', 'grad_norm': '1.377', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}       
{'loss': '0.1652', 'grad_norm': '11.39', 'learning_rate': '8.801e-06', 'epoch': '1.262'}       
{'loss': '0.1339', 'grad_norm': '2.718', 'learning_rate': '5.056e-06', 'epoch': '1.578'}       
{'loss': '0.1193', 'grad_norm': '32.86', 'learning_rate': '1.311e-06', 'epoch': '1.894'}       
{'train_runtime': '89.72', 'train_samples_per_second': '225.6', 'train_steps_per_second': '7.067', 'train_loss': '0.4062', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [01:29<00:00,  7.07it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:01<00:00, 25.75it/s]
  [google/electra-small-discriminator] held out ling_ham           n= 1500  unseen=0.981
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 18363.69it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.172', 'grad_norm': '2.861', 'learning_rate': '1.98e-05', 'epoch': '0.3165'}        
{'loss': '0.4375', 'grad_norm': '1.64', 'learning_rate': '1.628e-05', 'epoch': '0.6329'}       
{'loss': '0.155', 'grad_norm': '0.7382', 'learning_rate': '1.252e-05', 'epoch': '0.9494'}      
{'loss': '0.1052', 'grad_norm': '18.44', 'learning_rate': '8.759e-06', 'epoch': '1.266'}       
{'loss': '0.07931', 'grad_norm': '0.3771', 'learning_rate': '5e-06', 'epoch': '1.582'}         
{'loss': '0.06797', 'grad_norm': '0.6325', 'learning_rate': '1.241e-06', 'epoch': '1.899'}     
{'train_runtime': '89.45', 'train_samples_per_second': '226.1', 'train_steps_per_second': '7.066', 'train_loss': '0.322', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 632/632 [01:29<00:00,  7.07it/s]
100%|██████████████████████████████████████████████████████████| 48/48 [00:01<00:00, 25.74it/s]
  [google/electra-small-discriminator] held out nazario            n= 1510  unseen=0.261
Loading weights: 100%|█████████████████████████████████████| 199/199 [00:00<00:00, 9812.22it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.121', 'grad_norm': '3.22', 'learning_rate': '1.98e-05', 'epoch': '0.363'}          
{'loss': '0.414', 'grad_norm': '1.704', 'learning_rate': '1.562e-05', 'epoch': '0.726'}        
{'loss': '0.1748', 'grad_norm': '0.9342', 'learning_rate': '1.119e-05', 'epoch': '1.087'}      
{'loss': '0.114', 'grad_norm': '47.7', 'learning_rate': '6.77e-06', 'epoch': '1.45'}           
{'loss': '0.1236', 'grad_norm': '32.92', 'learning_rate': '2.345e-06', 'epoch': '1.813'}       
{'train_runtime': '80.36', 'train_samples_per_second': '219.2', 'train_steps_per_second': '6.869', 'train_loss': '0.3637', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 552/552 [01:20<00:00,  6.87it/s]
100%|██████████████████████████████████████████████████████████| 99/99 [00:04<00:00, 24.13it/s]
  [google/electra-small-discriminator] held out nigerian           n= 3140  unseen=0.021
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 11732.40it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.262', 'grad_norm': '3.419', 'learning_rate': '1.98e-05', 'epoch': '0.3289'}        
{'loss': '0.575', 'grad_norm': '2.196', 'learning_rate': '1.61e-05', 'epoch': '0.6579'}        
{'loss': '0.287', 'grad_norm': '28.77', 'learning_rate': '1.217e-05', 'epoch': '0.9868'}       
{'loss': '0.1553', 'grad_norm': '0.8367', 'learning_rate': '8.228e-06', 'epoch': '1.316'}      
{'loss': '0.1467', 'grad_norm': '3.728', 'learning_rate': '4.291e-06', 'epoch': '1.645'}       
{'loss': '0.1118', 'grad_norm': '0.5869', 'learning_rate': '3.543e-07', 'epoch': '1.974'}      
{'train_runtime': '93.71', 'train_samples_per_second': '207.4', 'train_steps_per_second': '6.488', 'train_loss': '0.4199', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 608/608 [01:33<00:00,  6.49it/s]
100%|██████████████████████████████████████████████████████████| 63/63 [00:02<00:00, 24.57it/s]
  [google/electra-small-discriminator] held out spamassassin_ham   n= 2000  unseen=0.993
Loading weights: 100%|████████████████████████████████████| 199/199 [00:00<00:00, 15410.27it/s]
[transformers] ElectraForSequenceClassification LOAD REPORT from: google/electra-small-discriminator
Key                                               | Status     | 
--------------------------------------------------+------------+-
discriminator_predictions.dense_prediction.bias   | UNEXPECTED | 
discriminator_predictions.dense.bias              | UNEXPECTED | 
discriminator_predictions.dense_prediction.weight | UNEXPECTED | 
discriminator_predictions.dense.weight            | UNEXPECTED | 
classifier.dense.weight                           | MISSING    | 
classifier.out_proj.weight                        | MISSING    | 
classifier.out_proj.bias                          | MISSING    | 
classifier.dense.bias                             | MISSING    | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
{'loss': '1.249', 'grad_norm': '2.756', 'learning_rate': '1.98e-05', 'epoch': '0.316'}         
{'loss': '0.5515', 'grad_norm': '2.159', 'learning_rate': '1.629e-05', 'epoch': '0.6319'}      
{'loss': '0.2456', 'grad_norm': '24.23', 'learning_rate': '1.255e-05', 'epoch': '0.9479'}      
{'loss': '0.1654', 'grad_norm': '0.6862', 'learning_rate': '8.801e-06', 'epoch': '1.262'}      
{'loss': '0.1196', 'grad_norm': '0.5403', 'learning_rate': '5.056e-06', 'epoch': '1.578'}      
{'loss': '0.1052', 'grad_norm': '0.4958', 'learning_rate': '1.311e-06', 'epoch': '1.894'}      
{'train_runtime': '93.22', 'train_samples_per_second': '217.1', 'train_steps_per_second': '6.801', 'train_loss': '0.3889', 'epoch': '2'}
100%|████████████████████████████████████████████████████████| 634/634 [01:33<00:00,  6.80it/s]
100%|██████████████████████████████████████████████████████████| 47/47 [00:01<00:00, 24.46it/s]
  [google/electra-small-discriminator] held out trec_ham           n= 1500  unseen=0.971

=== Leave-one-source-out: google/electra-small-discriminator ===
        held_out          measures    n  unseen_acc  normal_acc  seconds   drop
        ceas_ham legit specificity 1500      0.9787      0.9933       96 0.0146
       enron_ham legit specificity 3000      0.9837      0.9900       87 0.0063
        ling_ham legit specificity 1500      0.9813      1.0000       96 0.0187
         nazario   phishing recall 1510      0.2609      0.9603       96 0.6994
        nigerian   phishing recall 3140      0.0207      0.9841       89 0.9634
spamassassin_ham legit specificity 2000      0.9925      1.0000      101 0.0075
        trec_ham legit specificity 1500      0.9713      0.9933      100 0.0220
(unseen_acc: model trained without this source. normal_acc: normal run, source seen in training.)