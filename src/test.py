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
x = [1.0]*243
y = [1.0]*243
z = [1.0]*243
annot = [.0]*243
#x[3] = 3

#y[3] = 3

#z[3] = 3

#annot[3] = 2

a,b,c,d = alg1.alg_1(x,y,z,annot)

print a,b,c,d
