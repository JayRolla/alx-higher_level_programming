#!/usr/bin/python3
'Defines a class Square that allows accessing and updating the size.'

class Square:
    'Represents a square.'
    def __init__(self, size=0):
        'Initializes the square.'
        self.size = size  # This will call the size setter

    @property
    def size(self):
        'Retrieves the size of the square.'
        return self.__size

    @size.setter
    def size(self, value):
        'Sets the size of the square with validation.'
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        'Returns the area of the square.'
        return self.__size ** 2
