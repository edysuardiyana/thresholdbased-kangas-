import sv_tot

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


def micro_annotate(x_seq,y_seq,z_seq, annot):
    new_annot = []
    annot_flag = False
    x_buff = []
    y_buff = []
    z_buff = []
    annot_buff = []
    for i in range(len(x_seq)):
        if annot[i] in FALL_SET:
            x_buff.append(x_seq[i])
            y_buff.append(y_seq[i])
            z_buff.append(z_seq[i])
            annot_buff.append(annot[i])
        else:
            if len(x_buff) > 0:
                _,_,index_max = sv_tot.check_max(x_buff, y_buff, z_buff)
                del x_buff[:]
                del y_buff[:]
                del z_buff[:]
                for j in range(len(annot_buff)):
                    if j == index_max:
                        new_annot.append(2) # fall annotation
                    else:
                        new_annot.append(0)
                del annot_buff[:]
                new_annot.append(annot[i])
            else:
                new_annot.append(annot[i])
    return new_annot
