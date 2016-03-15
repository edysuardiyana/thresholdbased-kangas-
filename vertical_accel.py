import operator

def vertical_accel(SV_tot, SV_d):
    G = 1
    a_vert_seq = []
    for i in range(len(SV_tot)):
        a_vertical = ((SV_tot[i]*SV_tot[i])-(SV_d[i]*SV_d[i])-(G*G))/2 * G # this is a formula from Kangas et al.(2008)
        a_vert_seq.append(a_vertical)
    _, max_z_val = max(enumerate(a_vert_seq),key=operator.itemgetter(1))

    return max_z_val
