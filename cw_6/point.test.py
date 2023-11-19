# point_test.py
import unittest
from point import Point

class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_str(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

    def test_repr(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(1, 2)")

    def test_eq(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_ne(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertFalse(p1 != p2)
        self.assertTrue(p1 != p3)

    def test_add(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 - p2
        self.assertEqual(result, Point(-2, -2))

    def test_mul(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 * p2
        self.assertEqual(result, 11)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1.cross(p2)
        self.assertEqual(result, -2)

    def test_length(self):
        p = Point(3, 4)
        result = p.length()
        self.assertEqual(result, 5.0)

    def test_hash(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertEqual(hash(p1), hash(p2))
        self.assertNotEqual(hash(p1), hash(p3))

if __name__ == '__main__':
    unittest.main()
