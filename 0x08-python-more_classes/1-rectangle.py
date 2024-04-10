#!/usr/bin/python3
"""
Defines a class Rectangle with private instance attributes width and height,
and property and setter methods for them.
"""
class Rectangle:
    """
    Represents a rectangle, allowing for width and height to be securely set and retrieved.
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle, ensuring it is an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle, ensuring it is an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
