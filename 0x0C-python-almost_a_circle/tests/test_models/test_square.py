#!/usr/bin/python3
"""Unit tests for the Square class.

Tests the creation and functionality of the Square class, ensuring that
attributes and methods function as expected, consistent with its parent
class Rectangle.
"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Tests the functionality of the Square class."""
    
    def test_size_setter(self):
        """Test setting size also sets width and height in Square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_area_calculation(self):
        """Test the area method for Square."""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

if __name__ == "__main__":
    unittest.main()
