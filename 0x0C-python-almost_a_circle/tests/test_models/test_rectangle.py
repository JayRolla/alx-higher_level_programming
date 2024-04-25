#!/usr/bin/python3
"""Unit tests for the Rectangle class.

Tests the creation and functionality of the Rectangle class, ensuring that
attributes are set correctly and area calculations are accurate.
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests the functionality of the Rectangle class."""
    
    def test_width_setter(self):
        """Test that the width is set correctly with positive values."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)

    def test_area_calculation(self):
        """Test the area method returns correct values."""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)

if __name__ == "__main__":
    unittest.main()
