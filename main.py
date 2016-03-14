import matplotlib.pyplot as plt
import vertical_accel
import dynamic_sum_vector
import median_filter

def read_sequence():
    path = "/Users/ArseneLupin/Documents/edy/thresholdbased-kangas-/standing_example.csv"
    win_length = 3
    data_seq = []
    x_seq = []
    y_seq = []
    z_seq = []
    with open(path) as obj:
        for line in obj:
            raw_data = line.split(",")
            numeric_value = float(raw_data[6])
            x_val = float(raw_data[0])
            y_val = float(raw_data[1])
            z_val = float(raw_data[2])
            data_seq.append(numeric_value)
            x_seq.append(x_val)
            y_seq.append(y_val)
            z_seq.append(z_val)

        #filter the data using median filter with window length = 3
        data_seq_filt = median_filter.median_filter(x_seq, win_length)
        x_median = median_filter.median_filter(x_seq, win_length)
        y_median = median_filter.median_filter(y_seq, win_length)
        z_median = median_filter.median_filter(z_seq, win_length)
    return data_seq_filt, x_median, y_median, z_median

def main():
    order = 2
    cut_off = 0.25
    win_length = 3
    data_seq, x_seq, y_seq, z_seq = read_sequence()

    svd_seq = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq, order, cut_off)
    z_seq = vertical_accel.vertical_accel(data_seq,svd_seq)
    plt.plot(svd_seq)
    plt.show()





    #median_filtered = signal.medfilt(data_seq,3) # do median filter before further processing
    #filtered_data = digital_filter(order, cut_off, median_filtered)
    #without_median = digital_filter(order, cut_off, data_seq)

    #plt.plot(data_seq,'r')
    #plt.plot(filtered_data,'g')
    #plt.plot(without_median,'b')
    #plt.show()
if __name__ == '__main__':
    main()
