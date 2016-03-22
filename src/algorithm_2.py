# check the SV_tot, if lower than 0.6g, collect 1 s samples
# calculate the max value of samples above,
# * if vals > thresholds, collect data after 2s from Z and use low filter for that data
# * collect 0.4s samples from above
# * calculate the averages from data above
# * if the average <= 0.5 then the posture is lying

def alg_2(x_seq, y_seq, z_seq, annot):
    x_buff = []
    y_buff = []
    z_buff = []
    annot_buff = []


    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    #for i in range(len(x_seq)):
