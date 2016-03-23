import unittest
import src.algorithm_2 as alg2


class alg_2_test(unittest.TestCase):

    def alg_1_test(self):
        #test case for the integration
        #0 fall
        x = [0.5]* 500
        y = [0.5]* 500
        z = [0.5]* 500
        annot = [0]* 500

        TP, FP, TN, FN = alg2.alg_2(x,y,z,annot)

        self.assertEqual(TP,0)
        self.assertEqual(FP,0)
        self.assertEqual(TN,500)
        self.assertEqual(FN,0)

    def alg_2_test(self):
        #test case for the integration
        #1 falls only
        x = [0.5]* 500
        y = [0.5]* 500
        z = [0.5]* 500
        annot = [0]* 500

        x[0] = 0.03
        x[1] = 3
        #x[201] = 4

        y[0] = 0.03
        y[1] = 3
        #y[201] = 4


        z[0] = 0.03
        z[1] = 3
        #z[201] = 4

        annot[1] = 2
        #annot[201] = 2

        TP, FP, TN, FN = alg2.alg_2(x,y,z,annot)

        self.assertEqual(TP,1)
        self.assertEqual(FP,0)
        self.assertEqual(TN,498)
        self.assertEqual(FN,1)
