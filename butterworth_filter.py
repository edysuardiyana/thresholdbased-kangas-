#this is source codes for butterworth filter
from scipy import signal

def butter_high_pass(order,cut_off):
    b ,a = signal.butter(order,cut_off,"high", output='ba')
    return b, a

def butter_low_pass(order,cut_off):
    b ,a = signal.butter(order,cut_off, output='ba')
    return b, a

def digital_filter(order, cut_off, data_seq):
    b,a = butter_pass(order, cut_off)
    filtered_data = signal.lfilter(b,a,data_seq)
    #creating filter
    return filtered_data
