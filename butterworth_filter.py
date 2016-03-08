#this is source codes for butterworth filter

from scipy import signal
import matplotlib.pyplot as plt
import random as rd

def butter_pass(order, fc):
    b ,a = signal.butter(order,fc,'low', analog = True)
    return b, a

def digital_filter(b,a,data_seq):
    sig_output = signal.lfilter(b,a,data_seq,axis = -1, zi = None)
    return sig_output

def main():
    #testing butter filter
    b, a = butter_pass(2,0.25)
    print b, a

    data_seq = [1.5]*200
    #print data_seq

    data_seq[3] = 3.5
    data_seq[4] = 5
    data_seq[5] = 4.5
    data_seq[7] = 6
    data_seq[8] = 3.5

    for i in range(10,40):
        data_seq[i] = 2.5

    for i in range(50,100):
        data_seq[i] = 3

    sig_output = digital_filter(b , a, 100)


    print sig_output
    plt.plot(data_seq)
    plt.plot(sig_output)
    plt.show()


if __name__ == '__main__':
    main()
