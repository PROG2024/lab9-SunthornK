"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class CircleTest(unittest.TestCase):

    def test_add_area_valid_value(self):
        circle1 = Circle(2)
        circle2 = Circle(3)
        circle3 = Circle((2 ** 2 + 3 ** 2) ** 0.5)
        self.assertEqual(circle1.add_area(circle2).get_area(), circle3.get_area())
        self.assertEqual(circle1.add_area(circle2).get_radius(),circle3.get_radius())

    def test_add_area_edge_case(self):
        circle1 = Circle(0)
        circle2 = Circle(3)
        circle3 = Circle((0 ** 2 + 3 ** 2) ** 0.5)
        self.assertEqual(circle1.add_area(circle2).get_area(), circle3.get_area())
        self.assertEqual(circle1.add_area(circle2).get_radius(), circle3.get_radius())

    def test_negative_radius(self):
        with self.assertRaises(Exception):
            circle = Circle(-99)