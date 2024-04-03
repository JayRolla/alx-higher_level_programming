#!/usr/bin/python3
'Defines a class Square that can have a specific position.'

class Square:
    'Represents a square with a position.'
    def __init__(self, size=0, position=(0, 0)):
        'Initializes the square with size and position.'
        self.size = size
        self.position = position

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

    @property
    def position(self):
        'Retrieves the position.'
        return self.__position

    @position.setter
    def position(self, value):
        'Sets the position with validation.'
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        'Returns the area.'
        return self.__size ** 2

    def my_print(self):
        'Prints the square at its position.'
        if self.__size == 0:
            print()
            return
        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
