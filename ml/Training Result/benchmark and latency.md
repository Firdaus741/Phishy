**(.venv) PS D:\\Phishy> python ml\\benchmark.py baselines**

**Data: D:\\Phishy\\ml\\data\\unified\\unified.csv**

**train=11320 test=1415 (English only)**



&#x20;      **model    acc   prec    rec     f1    fpr  fp  fn  wrong  train\_s**

**tfidf\_logreg 0.9908 0.9956 0.9763 0.9859 0.0021   2  11     13      7.2**

**tfidf\_linsvm 0.9922 0.9978 0.9785 0.9881 0.0011   1  10     11      7.1**

&#x20;   **tfidf\_nb 0.9915 0.9935 0.9806 0.9870 0.0032   3   9     12      6.6**

**(.venv) PS D:\\Phishy> python ml\\benchmark.py loso**

**Data: D:\\Phishy\\ml\\data\\unified\\unified.csv**

**sources: \['ceas\_ham', 'enron\_ham', 'ling\_ham', 'nazario', 'nigerian', 'spamassassin\_ham', 'trec\_ham']**



&#x20; **\[tfidf\_logreg] held out ceas\_ham           n= 1500  unseen=0.983**

&#x20; **\[tfidf\_logreg] held out enron\_ham          n= 3000  unseen=0.997**

&#x20; **\[tfidf\_logreg] held out ling\_ham           n= 1500  unseen=0.989**

&#x20; **\[tfidf\_logreg] held out nazario            n= 1510  unseen=0.037**

&#x20; **\[tfidf\_logreg] held out nigerian           n= 3140  unseen=0.005**

&#x20; **\[tfidf\_logreg] held out spamassassin\_ham   n= 2000  unseen=0.998**

&#x20; **\[tfidf\_logreg] held out trec\_ham           n= 1500  unseen=0.993**



**=== Leave-one-source-out: tfidf\_logreg ===**

&#x20;       **held\_out          measures    n  unseen\_acc  normal\_acc  seconds   drop**

&#x20;       **ceas\_ham legit specificity 1500      0.9833      1.0000        6 0.0167**

&#x20;      **enron\_ham legit specificity 3000      0.9967      0.9967        6 0.0000**

&#x20;       **ling\_ham legit specificity 1500      0.9893      1.0000        6 0.0107**

&#x20;        **nazario   phishing recall 1510      0.0371      0.9536        6 0.9165**

&#x20;       **nigerian   phishing recall 3140      0.0054      0.9873        6 0.9819**

**spamassassin\_ham legit specificity 2000      0.9975      1.0000        6 0.0025**

&#x20;       **trec\_ham legit specificity 1500      0.9933      0.9933        6 0.0000**

**(unseen\_acc: model trained without this source. normal\_acc: normal run, source seen in training.)**



**(.venv) PS D:\\Phishy> python ml\\benchmark.py latency**

**CPU only | torch threads: 8 | 100 test emails, one at a time**



**Loading weights: 100%|██████████████████████████████████████| 201/201 \[00:00<00:00, 539.28it/s]**

&#x20; **done bert-base-uncased**

**Loading weights: 100%|██████████████████████████████████████| 104/104 \[00:00<00:00, 676.60it/s]**

&#x20; **done distilbert-base-uncased**

**Loading weights: 100%|█████████████████████████████████████| 203/203 \[00:00<00:00, 4194.37it/s]**

&#x20; **done electra-small-discriminator**

**Loading weights: 100%|█████████████████████████████████████| 201/201 \[00:00<00:00, 2539.02it/s]**

&#x20; **done MiniLM-L12-H384-uncased**

**Loading weights: 100%|██████████████████████████████████████| 201/201 \[00:00<00:00, 574.97it/s]**

&#x20; **done roberta-base**



&#x20;                     **model        type  params\_M  size\_MB  median\_ms  p95\_ms**

&#x20;              **tfidf\_logreg   classical       NaN      9.8       1.14    2.61**

&#x20;              **tfidf\_linsvm   classical       NaN      9.8       0.93    1.77**

&#x20;                  **tfidf\_nb   classical       NaN     16.2       1.95    3.12**

&#x20;         **bert-base-uncased transformer     109.5    438.0     177.62  202.38**

&#x20;   **distilbert-base-uncased transformer      67.0    267.8      91.08  102.98**

**electra-small-discriminator transformer      13.5     54.2      34.75   43.21**

&#x20;   **MiniLM-L12-H384-uncased transformer      33.4    133.5      59.02   70.49**

&#x20;              **roberta-base transformer     124.6    498.6     175.96  201.81**

**(.venv) PS D:\\Phishy> python ml\\benchmark.py latencypython ml\\benchmark.py latency**

