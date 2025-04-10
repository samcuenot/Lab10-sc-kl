# https://github.com/samcuenot/Lab10-sc-kl.git
# Partner 1: Samantha Cuenot
# Partner 2: Kayla Le

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(-1,4), 3)
        self.assertEqual(add(-1,-2), -3)
        self.assertEqual(add(0,1), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,5), -1)
        self.assertEqual(subtract(5,4), 1)
        self.assertEqual(subtract(100,50), 50)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(2, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(5, 20), 4)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)


    def test_logarithm(self): # 3 assertions
        # fill in code
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(8,2), 3)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(10000, 10), 4)
        self.assertEqual(logarithm(32768, 2), 15)


    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            logarithm(5,0)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(9), 3.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()