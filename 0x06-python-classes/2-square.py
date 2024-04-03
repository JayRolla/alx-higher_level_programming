#!/usr/bin/python3
'Defines a class Square with a validated private instance attribute size.'

class Square:
    'Represents a square with size validation.'
    def __init__(self, size=0):
        'Initializes the square with size validation.'
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
