#!/usr/bin/python3
'Defines a class Square that includes a method to print the square.'

class Square:
    'Represents a square that can print itself.'
    def __init__(self, size=0):
        'Initializes the square.'
        self.size = size

    @property
    def size(self):
        'Retrieves the size.'
        return self.__size

    @size.setter
    def size(self, value):
        'Sets the size with validation.'
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        'Returns the area.'
        return self.__size ** 2

    def my_print(self):
        'Prints the square with # characters.'
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
