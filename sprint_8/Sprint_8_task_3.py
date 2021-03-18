import unittest
import math


def quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    try:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
    except:
        raise ValueError
    if D == 0:
        return x1
    return x1, x2


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_1(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))

    def test_discriminant_2(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_discriminant_3(self):
        self.assertEqual(quadratic_equation(4, 1, 2), None)
