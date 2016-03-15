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

WIN_LENGTH = 3
ORDER = 2
CUT_OFF = 0.25
#thresholds for sensors that were strapped on the waist
THRESHOLD_SV_TOT = 2.0
THRESHOLD_SV_D = 1.7
THRESHODL_Z = 1.5
THRESHOLD_MINMAX = 2.0


def check_first_feat(x_seq,y_seq,z_seq):
    detect_flag = False
    sv_tot_seq, sv_tot_max = sv_tot.check_max(x_seq, y_seq, z_seq)
    sv_d_seq, sv_d_x = dynamic_sum_vector.dynamic_sum_vector(x_seq, y_seq, z_seq)
    sv_max_min = sv_minmax.calc_sv_max_min(x_seq, y_seq, z_seq)
    z_val = vertical_accel.vertical_accel(sv_tot_seq, sv_d_seq)

    if sv_tot_max > THRESHOLD_SV_TOT or sv_d_max > THRESHOLD_SV_D or sv_max_min >THRESHOLD_MINMAX or z_val > THRESHODL_Z:
        detect_flag = True

    return detect_flag

def alg_1(freq_rate, data_seq):
    win_length = 0.1 * freq_rate
    buffer_array = []
    detect_flag = False
    for i in range(len(data_seq)):
        buffer_array.append(data_seq[i])

        if len(buffer_array)>= win_length and not detect_flag:
            detect_flag = check_first_feat(data_seq[0:win_length])
