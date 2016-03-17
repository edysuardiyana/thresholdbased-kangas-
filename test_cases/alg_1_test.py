import unittest
import os
import sys
import algorithm_1

#print sys.path

class alg_1_test(unittest.TestCase):
    def no_peak_test(self):
        x_seq = [0]*1000
        y_seq = [0]*1000
        z_seq = [0]*1000
        annot_seq = [0]*1000

        TP, FP, TN, FN = algorithm_1.alg_1(x_seq,y_seq,z_seq,annot_seq)
        self.assertEqual(TP, 0.0)
        self.assertEqual(FP, 0.0)
        self.assertEqual(FP, 0.0)
        self.assertEqual(FP, 0.0)
