import unittest
from point import Point
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1, rect2)

    def test_ne(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertNotEqual(rect1, rect2)

    def test_center(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.center(), Point(2.0, 3.0))

    def test_area(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.area(), 4)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(1, 1)
        self.assertEqual(str(rect), "[(2, 3), (4, 5)]")

    def test_intersection(self):
        rect1 = Rectangle(1, 1, 3, 3)
        rect2 = Rectangle(2, 2, 4, 4)
        intersection_rect = rect1.intersection(rect2)
        self.assertEqual(str(intersection_rect), "[(2, 2), (3, 3)]")

    def test_cover(self):
        rect1 = Rectangle(1, 1, 3, 3)
        rect2 = Rectangle(2, 2, 4, 4)
        cover_rect = rect1.cover(rect2)
        self.assertEqual(str(cover_rect), "[(1, 1), (4, 4)]")

    def test_make4(self):
        rect = Rectangle(0, 0, 4, 4)
        small_rects = rect.make4()
        expected_small_rects = [
            Rectangle(0, 2, 2, 4),
            Rectangle(2, 2, 4, 4),
            Rectangle(0, 0, 2, 2),
            Rectangle(2, 0, 4, 2)
        ]
        for small_rect, expected_rect in zip(small_rects, expected_small_rects):
            self.assertEqual(small_rect, expected_rect)


if __name__ == '__main__':
    unittest.main()
