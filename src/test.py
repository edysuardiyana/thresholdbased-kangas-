import algorithm_1 as alg

x = [[True,2], [True,2], [True,2], [True,2], [True,2], [False,0], [False, 0],[False,3]]

TP,FP,TN,FN = alg.calc_metrics(x, "edy")
print TP
print FP
print TN
print FN
