import unittest
import calculator as calc

class tests (unittest.TestCase):

    def testAddition (self):
        self.assertEqual(calc.addition(78, 23), 101)
        self.assertEqual(calc.addition(6367, 8891), 15258)
        self.assertEqual(calc.addition(-30, 135), 105)

    def testSubtraction (self):
        self.assertEqual(calc.subtraction(20, 10), 10)
        self.assertEqual(calc.subtraction(50, -20), 70)
        self.assertEqual(calc.subtraction(7800, 2200), 5600)

    def testMultiplication (self):
        self.assertEqual(calc.multiplication(2, 25), 50)
        self.assertEqual(calc.multiplication(-5, 8), -40)
        self.assertEqual(calc.multiplication(2300, 3), 6900)

    def testDivision (self):
        self.assertEqual(calc.divison(60, 3), 20)
        self.assertEqual(calc.divison(-6, 2), -3)
        self.assertEqual(calc.divison(6400, 100), 64)

    def testInvert (self):
        self.assertEqual(calc.invert(5), -5)
        self.assertEqual(calc.invert(-90), 90)
        self.assertEqual(calc.invert(53450), -53450)

    def testExponent (self):
        self.assertEqual(calc.exponent(6, 2), 36)
        self.assertEqual(calc.exponent(4, 3), 64)
        self.assertEqual(calc.exponent(6, 9), 10077696)

if __name__ == '__main__':
    unittest.main()