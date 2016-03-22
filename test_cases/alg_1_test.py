import unittest
import os
import sys
import src.algorithm_1 as alg
import src.butterworth_filter as bwf
import src.sv_tot as svt
import src.sv_minmax as minmax
import math
import micro_annot

#print sys.path

class alg_1_test(unittest.TestCase):
    def no_peak_test(self):
        x_seq = [0]*1000
        y_seq = [0]*1000
        z_seq = [0]*1000
        annot_seq = [0]*1000

        TP, FP, TN, FN = alg.alg_1(x_seq,y_seq,z_seq,annot_seq)
        self.assertEqual(TP, 0.0)
        self.assertEqual(FP, 0.0)
        self.assertEqual(FP, 0.0)
        self.assertEqual(FP, 0.0)

    def butterworth_filteer_test(self):
        x_seq = [0]*1000
        x_seq[50] = 3.5
        x_seq[30] = -1.5
        filt = bwf.low_filter(2,0.25, x_seq)
        max_val = max(filt)
        self.assertAlmostEqual(max_val, 1.17587211788)

    def sv_tot_test_1(self):
        #for flat data
        x_seq = [0]*100
        y_seq = [0]*100
        z_seq = [0]*100

        data, max_v, index = svt.check_max(x_seq, y_seq, z_seq)
        self.assertEqual(len(data), len(x_seq))
        self.assertEqual(0,max_v)
        self.assertEqual(0,index)

    def sv_tot_test_2(self):
        #for flat data
        x_seq = [0]*10
        y_seq = [0]*10
        z_seq = [0]*10

        x_seq[5] = 3
        y_seq[5] = 4
        z_seq[5] = 5

        data, max_v, index = svt.check_max(x_seq, y_seq, z_seq)
        self.assertEqual(len(data), len(x_seq))
        self.assertAlmostEqual(max_v,math.sqrt(50))
        self.assertEqual(index,5)

    def sv_min_max_test(self):
        #test case for calculating difference between min and max
        x_seq = [8]*10
        y_seq = [18]*10
        z_seq = [22]*10

        x_seq[3] = 10
        x_seq[8] = 7

        y_seq[3] = 20
        y_seq[8] = 16

        z_seq[3] = 25
        z_seq[8] = 20

        minmax_val = minmax.calc_sv_max_min(x_seq, y_seq, z_seq)

        self.assertAlmostEqual(minmax_val, math.sqrt(50))

    def alg_1_test(self):
        #test case for the integration
        # 1 segment containing fall
        # assumption: the data has been filtered by median filter
        x = [1.0]*250
        y = [1.0]*250
        z = [1.0]*250

        x[3] = 3
        x[4] = 3.5
        x[5] = 4
        x[6] = 3.25

        y[3] = 3
        y[4] = 3.5
        y[5] = 4
        y[6] = 3.25

        z[3] = 3
        z[4] = 3.5
        z[5] = 4
        z[6] = 3.25

        annot = [2]*250

        TP, FP, TN, FN = alg.alg_1(x,y,z,annot)

        self.assertEqual(TP,1)
        self.assertEqual(FP,0)
        self.assertEqual(TN,0)
        self.assertEqual(FN,0)

    def alg_2_test(self):
        #test case for the integration
        x = [1.0]*480
        y = [1.0]*480
        z = [1.0]*480
        annot = [0]*480

        x[0] = 4
        x[1] = 5
        x[2] = 6

        y[0] = 4
        y[1] = 5
        y[2] = 6

        z[0] = 4
        z[1] = 5
        z[2] = 6

        annot[0] = 2

        TP, FP, TN, FN = alg.alg_1(x,y,z,annot)

        self.assertEqual(TP,0)
        self.assertEqual(FP,1)
        self.assertEqual(TN,23)
        self.assertEqual(FN,0)

    def micro_test(self):
        x = [0]*20
        y = [0]*20
        z = [0]*20
        annot = [0]*20

        for i in range(0,5):
            annot[i] = 2

        x[0] = 100
        y[0] = 100
        z[0] = 100

        for j in range(10,15):
            annot[j] = 2

        x[12] = 100
        y[12] = 100
        z[12] = 100


        new_annot = micro_annot.micro_annotate(x,y,z,annot)

        self.assertEqual(new_annot[0],2)
        self.assertEqual(new_annot[12],2)
        self.assertEqual(new_annot[3],0)
        self.assertEqual(new_annot[11],0)
