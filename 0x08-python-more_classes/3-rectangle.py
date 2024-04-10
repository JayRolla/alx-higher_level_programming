#!/usr/bin/python3
"""
Implements the __str__ method to define the string representation of a Rectangle instance.
"""
class Rectangle:
    # Previous methods unchanged.

    def __str__(self):
        """
        Returns a string representation of the Rectangle with the character '#' forming the shape.
        Returns:
            The visual representation of the rectangle using '#' characters.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = []
        for i in range(self.height):
            rectangle_str.append("#" * self.width)
        return "\n".join(rectangle_str)
