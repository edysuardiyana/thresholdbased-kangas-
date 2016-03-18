import operator

import butterworth_filter as bwf
from scipy import signal
import matplotlib.pyplot as plt

import median_filter
import vertical_accel as zv
import dynamic_sum_vector as svd
import sv_tot as svt


x = [0]*10
y = [0]*10
z = [0]*10

x[5] = 3.5
y[5] = 3.5
z[5] = 3.5

svd,_ = svd.dynamic_sum_vector(x,y,z)
svt,_,_ = svt.check_max(x,y,z)

z_seq,_ = zv.vertical_accel(svt,svd)

#plt.plot(x_seq)
#plt.plot(filt_seq)
#plt.plot(tempf)
#plt.plot(y)
#plt.plot(z)
#plt.plot(svd)
plt.plot(svt,'r')
plt.plot(z_seq,'g')
plt.show()
