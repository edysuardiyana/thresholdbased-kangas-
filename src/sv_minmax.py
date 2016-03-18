import operator
import lnorm

def calc_sv_max_min(x_seq,y_seq,z_seq):
    sv_minmax = 0
    minmax_x = find_max_min(x_seq)
    minmax_y = find_max_min(y_seq)
    minmax_z = find_max_min(z_seq)

    sv_minmax = lnorm.l2norm(minmax_x,minmax_y,minmax_z)

    return sv_minmax


def find_max_min(seq):
    _, max_val = max(enumerate(seq),key=operator.itemgetter(1))
    _, min_val = min(enumerate(seq),key=operator.itemgetter(1))
    differ_maxmin = abs(max_val - min_val)
    return differ_maxmin
