#this is source code for algorithm 1
#IMPACT+POSTURE
# * use 0.1 s non-overlapped sliding window
# * calculate maximum value of SV_tot and SV_d and calculate the difference between SV_tot_max and sv_tot_min
# * compare the values above to the thresholdbased
# * if vals > thresholds, collect data after 2s from Z and use low filter for that data
# * collect 0.4s samples from above
# * calculate the averages from data above
# * if the average <= 0.5 then the posture is lying

# assumption: data that sent here has been filtered using median filter
import dynamic_sum_vector
import operator
import sv_tot
import sv_minmax
import vertical_accel
import butterworth_filter
import numpy as np
import matplotlib.pyplot as plt
import median_filter

#WINDOW LENGTH
MED_WIN = 3
WIN_LENGTH = 10 #0.1*freq_rate
WIN_LYING = 40 # 0.4*freq_rate
WIN_DELAY = 200 # 2* freq_rate

#thresholds for sensors that were strapped on the waist
THRESHOLD_SV_TOT = 2.0
THRESHOLD_SV_D = 1.7
THRESHODL_Z = 1.5
THRESHOLD_MINMAX = 2.0

ORDER = 2
CUT_OFF = 0.25

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

def check_first_feat(x_seq,y_seq,z_seq):
    detect_flag = False
    index_max = 0
    sv_tot_seq, sv_tot_max, index_max = sv_tot.check_max(x_seq, y_seq, z_seq)
    sv_d_seq, sv_d_max = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    sv_max_min = sv_minmax.calc_sv_max_min(x_seq, y_seq, z_seq)
    _,z_val = vertical_accel.vertical_accel(sv_tot_seq, sv_d_seq)
    #print "first check"
    if sv_tot_max > THRESHOLD_SV_TOT or sv_d_max > THRESHOLD_SV_D or sv_max_min >THRESHOLD_MINMAX or z_val > THRESHODL_Z:
        detect_flag = True

    return detect_flag, index_max

def check_second_feat(x_seq, y_seq, z_seq):
    #print "second check"
    fall_flag = False
    sv_d_seq, sv_d_x = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    filtered_data = butterworth_filter.low_filter(ORDER, CUT_OFF, sv_d_seq)
    np_filter = np.array(filtered_data)

    if np_filter.mean() <= 0.5:
        fall_flag = True

    return fall_flag

def alg_1(x_seq, y_seq, z_seq, annot_seq):
    detect_flag = False
    sec_feat_flag = False
    final_detec_flag = False
    expect_flag = False
    annot = 0


    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    while len(x_seq) >= WIN_LENGTH:
        result = 0
        if not sec_feat_flag:
            detect_flag, index_max = check_first_feat(x_seq[:WIN_LENGTH], y_seq[:WIN_LENGTH],z_seq[:WIN_LENGTH])
            sec_feat_flag = True
            annot = annot_seq[index_max]
        else:
            if detect_flag:
                if len(x_seq) >= index_max + WIN_DELAY + WIN_LYING:
                    init_win = index_max + WIN_DELAY
                    end_win = init_win + WIN_LYING
                    final_detec_flag = check_second_feat(x_seq[init_win:end_win], y_seq[init_win: end_win], z_seq[init_win: end_win])
                    del x_seq[:WIN_LENGTH]
                    del y_seq[:WIN_LENGTH]
                    del z_seq[:WIN_LENGTH]
                    del annot_seq[:WIN_LENGTH]
                    sec_feat_flag = False

                    #confusion matrix calculation
                    result = accuracy_check(annot, final_detec_flag)
                    if result == 1:
                        true_positive = true_positive + 1
                    elif result == 2:
                        false_positive = false_positive + 1
                    elif result == 3:
                        true_negative = true_negative + 1
                    elif result == 4:
                        false_negative = false_negative + 1
                else:
                    # the case where high peak was deteced in the first check but there is no more samples to process
                    del x_seq[:]
                    del y_seq[:]
                    del z_seq[:]
                    del annot_seq[:]

            else:

                del x_seq[:WIN_LENGTH]
                del y_seq[:WIN_LENGTH]
                del z_seq[:WIN_LENGTH]
                del annot_seq[:WIN_LENGTH]
                sec_feat_flag = False

                #confusion matrix calculation
                final_detec_flag = False
                result = accuracy_check(annot, final_detec_flag)
                if result==1:
                    true_positive = true_positive + 1
                elif result == 2:
                    false_positive = false_positive + 1
                elif result == 3:
                    true_negative = true_negative + 1
                elif result == 4:
                    false_negative = false_negative + 1

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
