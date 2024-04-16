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
