import butterworth_filter as bwf
import math

def dynamic_sum_vector(x_seq, y_seq, z_seq, order, cut_off):

    x_hp = bwf.digital_filter(order, cut_off, x_seq)
    y_hp = bwf.digital_filter(order, cut_off, x_seq)
    z_hp = bwf.digital_filter(order, cut_off, x_seq)

    svd_seq = []
    for i in range(len(x_hp)):
        sv_d = l2norm(x_hp[i], y_hp[i], z_hp[i])
        svd_seq.append(sv_d)

    return svd_seq

def l2norm(x, y, z):
    return math.sqrt(x * x + y * y + z * z)
