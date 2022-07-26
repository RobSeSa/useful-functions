import accuracy

'''
Exoplanet classification
CALCULATING METRICS...

   thresh = 0.50, precision = 0.92, recall = 0.91
      TN = 1183, FP = 30, FN = 32, TP = 328
   thresh = 0.60, precision = 0.92, recall = 0.89
      TN = 1185, FP = 28, FN = 38, TP = 322
   thresh = 0.70, precision = 0.94, recall = 0.86
      TN = 1195, FP = 18, FN = 52, TP = 308
   thresh = 0.80, precision = 0.95, recall = 0.76
      TN = 1200, FP = 13, FN = 87, TP = 273
   thresh = 0.90, precision = 0.97, recall = 0.62
      TN = 1205, FP = 8, FN = 137, TP = 223
'''

p = [0.92, 0.92, 0.94, 0.95, 0.97]
r = [0.91, 0.89, 0.86, 0.76, 0.62]

for precision, recall in zip(p, r):
    accuracy.f1_score(precision, recall)
