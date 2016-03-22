import operator

import butterworth_filter as bwf
from scipy import signal
import matplotlib.pyplot as plt

import median_filter
import vertical_accel as zv
import dynamic_sum_vector as svd
import sv_tot as svt

import algorithm_1 as alg1
#test case for the integration
# 1 segment containing fall
x = [0.5]* 500
y = [0.5]* 500
z = [0.5]* 500
annot = [0]* 500
x[3] = 3
x[4] = 4

y[3] = 3
y[4] = 4

z[3] = 3
z[4] = 4

annot[4] = 2

a,b,c,d = alg1.alg_1(x,y,z,annot)

print a,b,c,d
