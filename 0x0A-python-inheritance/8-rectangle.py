#!/usr/bin/python3
"""Rectangle Module"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer greater than 0

        Args:
            name: The name of the value being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with a given width and height

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object

        Returns:
            A string in the format '[Rectangle] <width>/<height>'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes the area of the Rectangle object

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height
