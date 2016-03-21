import operator

import butterworth_filter as bwf
from scipy import signal
import matplotlib.pyplot as plt

import median_filter
import vertical_accel as zv
import dynamic_sum_vector as svd
import sv_tot as svt

import algorithm_1 as alg1


x = [1.0]*480
y = [1.0]*480
z = [1.0]*480
annot = [2]*480

x[0] = 4

y[0] = 4

z[0] = 4

for i in range(49,480):
    annot[i] = 0
    x[i] = 4
    y[i] = 4
    z[i] = 4

a,b,c,d = alg1.alg_1(x,y,z,annot)

print a,b,c,d
