import unittest


class DivideTest(unittest.TestCase):
    def test_raises(self):
        self.assertRaises(ZeroDivisionError, Divide, 3, 0)

    def test_2(self):
        self.assertAlmostEqual(Divide(1,3), 0.333333, 6)

    def test_3(self):
        self.assertIsNotNone(Divide(0,1))

    def test_4(self):
        self.assertEqual(Divide(10,2), 5)


def Divide(num1, num2):
    return float(num1)/num2
