#!/usr/bin/python3
"""
Expands 1-rectangle with methods to calculate the rectangle's area and perimeter.
"""
class Rectangle:
    # Previous methods unchanged.

    def area(self):
        """
        Calculates the area of the Rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle.
        Returns:
            The perimeter of the rectangle, or 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
