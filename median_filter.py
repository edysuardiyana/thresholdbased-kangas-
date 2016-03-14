from scipy import signal
def median_filter(data, kernel):
    median_filtered = signal.medfilt(data,kernel) # do median filter before further processing
    return median_filtered
