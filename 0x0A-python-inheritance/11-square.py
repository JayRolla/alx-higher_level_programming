#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square
    """

    def __init__(self, size):
        """
        Initializes the square

        Args:
            size (int): The size of the square
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square

        Returns:
            str: A string representation of the square in the format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.width, self.height)
