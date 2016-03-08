#exercise for convolution

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


x = [0,-1,-1.5,2,1.5,1.5,0.5,0,-0.5] # this is x[n]

h = [1,0.5,0.75,0.95] #this is h[n]

y = [0]*(len(x)+len(h)-1) #this is the output signal

for i in range(len(x)):
    for j in range(len(h)):
        y[i+j] = y[i+j]+x[i]*h[j]

plt.plot(x)
plt.show()
plt.plot(h)
plt.show()
plt.plot(y)
plt.show()
