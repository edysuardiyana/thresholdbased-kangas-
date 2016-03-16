#this is source codes for butterworth filter
from scipy import signal

def high_filter(order, cut_off, data_seq):
    b ,a = signal.butter(order,cut_off,"high", output='ba')
    filtered_data = signal.lfilter(b,a,data_seq)
    return filtered_data

def low_filter(order, cut_off, data_seq):
    b ,a = signal.butter(order,cut_off,"low", output='ba')
    filtered_data = signal.lfilter(b,a,data_seq)
    return filtered_data
