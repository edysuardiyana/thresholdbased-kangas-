#this is source code for algorithm 1
#IMPACT+POSTURE
# do the median filter first
# * use 0.1 s non-overlapped sliding window
# * calculate maximum value of SV_tot and SV_d and calculate the difference between SV_tot_max and sv_tot_min
# * compare the values above to the thresholdbased
# * if vals > thresholds, collect data after 2s from Z and use low filter for that data
# * collect 0.4s samples from above
# * calculate the averages from data above
# * if the average <= 0.5 then the posture is lying
import dynamic_sum_vector
import median_filter
import operator
import sv_tot
import sv_minmax
import vertical_accel
import butterworth_filter
import numpy as np

WIN_LENGTH = 0.1 * 100
WIN_LYING = 0.4 * 100
WIN_DELAY = 2 * 100
ORDER = 2
CUT_OFF = 0.25
#thresholds for sensors that were strapped on the waist
THRESHOLD_SV_TOT = 2.0
THRESHOLD_SV_D = 1.7
THRESHODL_Z = 1.5
THRESHOLD_MINMAX = 2.0


def check_first_feat(x_seq,y_seq,z_seq):
    detect_flag = False
    index_max = 0
    sv_tot_seq, sv_tot_max, index_max = sv_tot.check_max(x_seq, y_seq, z_seq)
    sv_d_seq, sv_d_x = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    sv_max_min = sv_minmax.calc_sv_max_min(x_seq, y_seq, z_seq)
    z_val = vertical_accel.vertical_accel(sv_tot_seq, sv_d_seq)

    if sv_tot_max > THRESHOLD_SV_TOT or sv_d_max > THRESHOLD_SV_D or sv_max_min >THRESHOLD_MINMAX or z_val > THRESHODL_Z:
        detect_flag = True

    return detect_flag, index_max

def check_second_feat(x_seq, y_seq, z_seq):
    fall_flag = False
    sv_d_seq, sv_d_x = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    filtered_data = butterworth_filter.low_filter(sv_d_seq)
    np_filter = np.array(filtered_data)
    if np_filter.mean() <= 0.5:
        fall_flag = True

    return fall_flag

def alg_1(freq_rate, x_seq, y_seq, z_seq, annot_seq):
    buffer_x = []
    buffer_y = []
    buffer_z = []
    buffer_annot = []
    detect_flag = False
    sec_feat_flag = False
    final_detec_flag = False
    annot = 0
    for i in range(len(x_seq)):

        buffer_x.append(x_seq[i])
        buffer_y.append(y_seq[i])
        buffer_z.append(z_seq[i])
        buffer_annot.append(annot_seq[i])

        if len(buffer_x)>= WIN_LENGTH:
            if not sec_feat_flag:
                detect_flag, index_max = check_first_feat(buffer_x[0:WIN_LENGTH], buffer_y[0:WIN_LENGTH], buffer_z[0:WIN_LENGTH])
                sec_feat_flag = True
                annot = annot_seq[index_max]
            else:
                if detect_flag:
                    if len(buffer_x) >= index_max + WIN_DELAY + WIN_LYING:
                        del buffer_x[:index_max+WIN_DELAY]
                        del buffer_y[:index_max+WIN_DELAY]
                        del buffer_z[:index_max+WIN_DELAY]
                        final_detec_flag = check_second_feat(buffer_x[:WIN_LYING], buffer_y[:WIN_LYING], buffer_z[:WIN_LYING])
                        del buffer_x[:index_max+WIN_LYING]
                        del buffer_y[:index_max+WIN_LYING]
                        del buffer_z[:index_max+WIN_LYING]
                        sec_feat_flag = False
                else:
                    del buffer_x[0:WIN_LENGTH]
                    del buffer_y[0:WIN_LENGTH]
                    del buffer_z[0:WIN_LENGTH]
                    sec_feat_flag = False
