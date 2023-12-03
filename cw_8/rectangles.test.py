import unittest
import os
from rectangles import Rectangle, Point


class TestRectangle(unittest.TestCase):

    def test_from_points(self):
        file_path = "test_input_data.txt"
        with open(file_path, "w") as file:
            file.write("1 2\n3 4\n")  # tworzenie "wirtualnego" pliku z danymi do testu

        rectangle = Rectangle.from_points(file_path)  # tworzenie obiektu Rectangle
        expected_rectangle = Rectangle(1, 2, 3, 4)  # Spodziewany wynik żeby nie działać na stringach tylko na obiektach
        self.assertEqual(rectangle, expected_rectangle)
        os.remove(file_path)

    def test_properties(self):
        rectangle = Rectangle(1, 2, 4, 6)
        self.assertEqual(rectangle.top, 6)
        self.assertEqual(rectangle.bottom, 2)
        self.assertEqual(rectangle.left, 1)
        self.assertEqual(rectangle.right, 4)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.topleft, Point(1, 6))
        self.assertEqual(rectangle.topright, Point(4, 6))
        self.assertEqual(rectangle.bottomleft, Point(1, 2))
        self.assertEqual(rectangle.bottomright, Point(4, 2))


if __name__ == '__main__':
    unittest.main()
