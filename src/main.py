import matplotlib.pyplot as plt
import vertical_accel
import dynamic_sum_vector
import median_filter
import algorithm_1
import algorithm_2
import algorithm_3

ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                                 ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')
WIN_LENGTH = 3

def read_sequence():
    path = "/Users/ArseneLupin/Documents/edy/thresholdbased-kangas-/standing_example.csv"
    data_seq = []
    x_seq = []
    y_seq = []
    z_seq = []
    annot_seq = []
    with open(path) as obj:
        for line in obj:
            raw_data = line.split(",")
            ori_data = [float(x) for x in raw_data[:len(raw_data)]]
            tupled_data = ARRAY_TUPLED(*ori_data)
            x_seq.append(tupled_data.AXC)
            y_seq.append(tupled_data.AYC)
            z_seq.append(tupled_data.AZC)
            annot_seq.append(tupled_data.ANNOT)

        x_median = median_filter.median_filter(x_seq, WIN_LENGTH)
        y_median = median_filter.median_filter(y_seq, WIN_LENGTH)
        z_median = median_filter.median_filter(z_seq, WIN_LENGTH)
    return x_median, y_median, z_median, annot_seq

def main():
    #order = 2
    #cut_off = 0.25
    #win_length = 3
    listname = []
    alg_1 = []
    alg_2 = []
    alg_3 = []

    x_seq, y_seq, z_seq = read_sequence()

    for name in listname:
        x_seq, y_seq, z_seq = read_sequence(name)
        #alg 1
        true_positive_1, false_positive_1, true_negative_1, false_negative_1 = algorithm_1.alg_1(x_seq, y_seq, z_seq)
        alg_1.append([true_positive_1, false_positive_1, true_negative_1, false_negative_1])

        #alg 2
        true_positive_2, false_positive_2, true_negative_2, false_negative_2 = algorithm_2.alg_2(x_seq, y_seq, z_seq)
        alg_2.append([true_positive_2, false_positive_2, true_negative_2, false_negative_2])

        #alg 3
        true_positive_3, false_positive_3, true_negative_3, false_negative_3 = algorithm_3.alg_3(x_seq, y_seq, z_seq)
        alg_3.append([true_positive_3, false_positive_3, true_negative_3, false_negative_3])









    #median_filtered = signal.medfilt(data_seq,3) # do median filter before further processing
    #filtered_data = digital_filter(order, cut_off, median_filtered)
    #without_median = digital_filter(order, cut_off, data_seq)

    #plt.plot(data_seq,'r')
    #plt.plot(filtered_data,'g')
    #plt.plot(without_median,'b')
    #plt.show()
if __name__ == '__main__':
    main()
