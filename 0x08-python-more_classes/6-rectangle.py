#!/usr/bin/python3
"""
Extends previous Rectangle definition by adding a class attribute that counts the
number of instances and a destructor method to decrement this count when an instance is destroyed.
"""
class Rectangle:
    # New class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance counter.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    # Other methods unchanged.

    def __del__(self):
        """
        Destructor method for Rectangle instances.
        Decrements the instance counter and prints a message when an instance is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
