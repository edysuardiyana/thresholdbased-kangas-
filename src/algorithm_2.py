# check the SV_tot, if lower than 0.6g, collect 1 s samples
# calculate the max value of samples above,
# * if vals > thresholds, collect data after 2s from Z/SV_TOT and use low filter for that data
# * collect 0.4s samples from above
# * calculate the averages from data above
# * if the average <= 0.5 then the posture is lying

# assumption: all data that sent here has been filtered using median filter

import lnorm
import sv_tot
import vertical_accel
import dynamic_sum_vector
import butterworth_filter
import numpy as np

FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])

PRE_IMP = 0.6 #0.6g
WIN_LENGTH = 100 # freq_rate*0.1 --> freq_rate = 100
WIN_DELAY = 200
WIN_LYING = 40
THRESHOLD_SV_TOT = 2.0
THRESHOLD_SV_D = 1.7
THRESHODL_Z = 1.5
ORDER = 2
CUT_OFF = 0.25



def first_check(x_seq, y_seq, z_seq):
    detect_flag = False
    index_max = 0
    sv_tot_seq, sv_tot_max, index_max = sv_tot.check_max(x_seq, y_seq, z_seq)
    sv_d_seq, sv_d_max = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    _,z_val = vertical_accel.vertical_accel(sv_tot_seq, sv_d_seq)
    #print "first check"
    if sv_tot_max > THRESHOLD_SV_TOT or z_val > THRESHODL_Z:
        detect_flag = True

    return detect_flag, index_max

def second_check(x_seq, y_seq, z_seq):
    #print "second check"
    fall_flag = False
    sv_d_seq, sv_d_x = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    filtered_data = butterworth_filter.low_filter(ORDER, CUT_OFF, sv_d_seq)
    np_filter = np.array(filtered_data)

    if np_filter.mean() <= 0.5:
        fall_flag = True

    return fall_flag

def alg_2(x_seq, y_seq, z_seq, annot):
    x_buff = []
    y_buff = []
    z_buff = []
    annot_buff = []


    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    annot_val = 0
    while len(x_seq)> 0:

        sv_tot_local = lnorm.l2norm(x_seq[0], y_seq[0], z_seq[0])
        if sv_tot_local < 0.6:
            detect_flag, index_max = first_check(x_seq[:WIN_LENGTH], y_seq[:WIN_LENGTH], z_seq[:WIN_LENGTH])
            annot_val = annot[index_max]
            if detect_flag:
                init_win = WIN_LENGTH + WIN_DELAY
                end_win = init_win + WIN_LYING
                final_flag = second_check(x_seq[init_win:end_win], y_seq[init_win:end_win], z_seq[init_win:end_win])
                result = accuracy_check(annot_val, final_flag)
                if result == 1:
                    true_positive = true_positive + 1
                elif result == 2:
                    false_positive = false_positive + 1
                elif result == 3:
                    true_negative = true_negative + 1
                elif result == 4:
                    false_negative = false_negative + 1

                del x_seq[0]
                del y_seq[0]
                del z_seq[0]
                del annot[0]
            else:

                final_flag = False
                result = accuracy_check(annot_val, final_flag)
                if result == 1:
                    true_positive = true_positive + 1
                elif result == 2:
                    false_positive = false_positive + 1
                elif result == 3:
                    true_negative = true_negative + 1
                elif result == 4:
                    false_negative = false_negative + 1

                del x_seq[0]
                del y_seq[0]
                del z_seq[0]
                del annot[0]
        else:
            detect_flag, index_max = first_check(x_seq[:WIN_LENGTH], y_seq[:WIN_LENGTH], z_seq[:WIN_LENGTH])
            annot_val = annot[index_max]
            final_flag = False
            result = accuracy_check(annot_val, final_flag)
            if result == 1:
                true_positive = true_positive + 1
            elif result == 2:
                false_positive = false_positive + 1
            elif result == 3:
                true_negative = true_negative + 1
            elif result == 4:
                false_negative = false_negative + 1

            del x_seq[0]
            del y_seq[0]
            del z_seq[0]
            del annot[0]

    return true_positive, false_positive, true_negative, false_negative

def accuracy_check(annot, final_detec_flag):
    result = 0

    if annot in FALL_SET and final_detec_flag:
        #true positive
        result = 1
    elif annot not in FALL_SET and final_detec_flag:
        #false positive
        result = 2
    elif annot not in FALL_SET and not final_detec_flag:
        #true negative
        result = 3
    else: #in Fall Set and not final_detec_flag
        #false negative
        result = 4
    return result
