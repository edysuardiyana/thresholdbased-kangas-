import operator

import butterworth_filter as bwf
from scipy import signal
import matplotlib.pyplot as plt

import median_filter
import vertical_accel as zv
import dynamic_sum_vector as svd
import sv_tot as svt

import algorithm_1 as alg1
import algorithm_2 as alg2
#test case for the integration
# 1 segment containing fall
x = [0.5]* 500
y = [0.5]* 500
z = [0.5]* 500
annot = [0]* 500

x[0] = 0.03
x[1] = 3
#x[201] = 4

y[0] = 0.03
y[1] = 3
#y[201] = 4


z[0] = 0.03
z[1] = 3
#z[201] = 4

for i in range(0,200):
    annot[i] = 2
#annot[201] = 2

a,b,c,d = alg2.alg_2(x,y,z,annot)

print a,b,c,d
