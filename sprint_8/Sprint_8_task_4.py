import unittest
import math


class TriangleNotValidArgumentException(Exception):
    def __init__(self):
        self.inf = "Can`t create triangle with this arguments"


class TriangleNotExistException(Exception):
    def __init__(self):
        self.inf = "Not valid arguments"


class Triangle:
    def __init__(self, lst):
        self.lst = lst

    def get_area(self):
        for l in self.lst:
            try:
                try:
                    z = int(l)
                except:
                    raise TriangleNotValidArgumentException
                if l != z:
                    raise TriangleNotValidArgumentException
                if len(self.lst) != 3:
                    raise TriangleNotValidArgumentException
                self.a = self.lst[0]
                self.b = self.lst[1]
                self.c = self.lst[2]
            except TriangleNotValidArgumentException as ms:
                return ms.inf

        p = (self.a + self.b + self.c) / 2
        try:
            try:
                res = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
                return res
            except:
                raise TriangleNotExistException
        except TriangleNotExistException as ms:
            return ms


class TriangleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Triangle([3, 4, 5]).get_area(), 6.0)

    def test_2(self):
        self.assertAlmostEqual(Triangle([10, 10, 10]).get_area(), 43.30, 2)

    def test_3(self):
        self.assertAlmostEqual(Triangle([6, 7, 8]).get_area(), 20.33, 2)



triangle = Triangle([3, 4, "5"])

print(triangle.get_area())
