import operator

import butterworth_filter as bwf
from scipy import signal
import matplotlib.pyplot as plt

import median_filter
import vertical_accel as zv
import dynamic_sum_vector as svd
import sv_tot as svt

import algorithm_1 as alg1


x = [1.0]*800
y = [1.0]*800
z = [1.0]*800

x[100] = 3
x[101] = 3.5
x[102] = 4
x[103] = 3.25

y[100] = 3
y[101] = 3.5
y[102] = 4
y[103] = 3.25

z[100] = 3
z[101] = 3.5
z[102] = 4
z[103] = 3.25

annot = [2]*800

a,b,c,d = alg1.alg_1(x,y,z,annot)
