#!/usr/bin/python3
"""
Allows the string representation of the Rectangle to be customized by changing the character used.
"""
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"  # New class attribute

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance, allowing for the print symbol to be customized.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle using a customizable character.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = []
        for i in range(self.height):
            rectangle_str.append(str(self.print_symbol) * self.width)
        return "\n".join(rectangle_str)
