import butterworth_filter as bwf
import math
import lnorm
ORDER = 2
CUT_OFF = 0.25
def dynamic_sum_vector(x_seq, y_seq, z_seq):

    x_hp = bwf.high_filter(ORDER, CUT_OFF, x_seq)
    y_hp = bwf.high_filter(ORDER, CUT_OFF, x_seq)
    z_hp = bwf.high_filter(ORDER, CUT_OFF, x_seq)

    svd_seq = []
    for i in range(len(x_hp)):
        sv_d = lnorm.l2norm(x_hp[i], y_hp[i], z_hp[i])
        svd_seq.append(sv_d)

    _, sv_d_max = max(enumerate(svd_seq),key=operator.itemgetter(1))

    return svd_seq, sv_d_max
