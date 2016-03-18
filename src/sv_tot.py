import lnorm
import operator

def check_max(x_seq, y_seq, z_seq):
    # finding SV_TOT
    sv_tot_data = []
    for i in range(len(x_seq)):
        sv_tot = lnorm.l2norm(x_seq[i], y_seq[i], z_seq[i])
        sv_tot_data.append(sv_tot)

    sv_max_index, sv_tot_max = max(enumerate(sv_tot_data),key=operator.itemgetter(1))
    
    return sv_tot_data, sv_tot_max, sv_max_index
