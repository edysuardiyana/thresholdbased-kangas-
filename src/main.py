# note for the author: just use scaled data from Staged-CC experiment

import matplotlib.pyplot as plt
import vertical_accel
import dynamic_sum_vector
import median_filter
import algorithm_1
import algorithm_2
import algorithm_3
from collections import namedtuple

import matplotlib.pyplot as plt

import micro_annot
import csv


ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                                 ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')
WIN_LENGTH = 3

def read_sequence(name):
    path = "/home/arsene-lupin/git/thresholdbased-kangas-/waist_scaled/"+name+".csv"
    data_seq = []
    x_seq = []
    y_seq = []
    z_seq = []
    annot_seq = []
    with open(path) as obj:
        for line in obj:
            raw_data = line.split()
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
    listname = read_name()
    alg_1 = []
    alg_2 = []
    alg_3 = []

    for name in listname:
        command_str = "testing "+name
        print command_str
        x_seq, y_seq, z_seq,annot = read_sequence(name)
        new_annot = micro_annot.micro_annotate(x_seq, y_seq, z_seq, annot)
        x_seq = x_seq.tolist()
        y_seq = y_seq.tolist()
        z_seq = z_seq.tolist()
        #write_output(x_seq, y_seq, z_seq, new_annot)
        #alg 1
        tp_1, fp_1, tn_1, fn_1 = algorithm_1.alg_1(name,x_seq, y_seq, z_seq, annot)
        alg_1.append([tp_1, fp_1, tn_1, fn_1])
        write_result(tp_1, fp_1, tn_1, fn_1)
        #alg 2
        #true_positive_2, false_positive_2, true_negative_2, false_negative_2 = algorithm_2.alg_2(x_seq, y_seq, z_seq)
        #alg_2.append([true_positive_2, false_positive_2, true_negative_2, false_negative_2])

        #alg 3
        #true_positive_3, false_positive_3, true_negative_3, false_negative_3 = algorithm_3.alg_3(x_seq, y_seq, z_seq)
        #alg_3.append([true_positive_3, false_positive_3, true_negative_3, false_negative_3])

    print "Work is done, Sir!"
def read_name():
    path = "/home/arsene-lupin/git/thresholdbased-kangas-/src/listname"
    name_list = []
    with open(path) as obj_name:
        for data in obj_name:
            raw = data.split()
            name_list.append(raw[0])
    return name_list

def write_result(tp,fp,tn,fn):
    path = "/home/arsene-lupin/git/thresholdbased-kangas-/result.csv"
    out_file = open(path, "a")
    csv_writer = csv.writer(out_file, delimiter='\t')
    temp = [tp,fp,tn,fn]
    csv_writer.writerow(temp)
    out_file.close()



################################################################################
def write_output(x_seq, y_seq, z_seq, annot):
    for i in range(len(x_seq)):
        path = "/home/edysuardiyana/edy/git/thresholdbased-kangas-/src/output_example.csv"
        out_file = open(path, "a")
        csv_writer = csv.writer(out_file, delimiter='\t')
        temp = [x_seq[i], y_seq[i], z_seq[i], annot[i]]
        csv_writer.writerow(temp)
        out_file.close()


if __name__ == '__main__':
    main()
