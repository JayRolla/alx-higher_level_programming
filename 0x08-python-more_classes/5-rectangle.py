#!/usr/bin/python3
"""
Adds a destructor method that prints a message when a Rectangle instance is deleted.
"""
class Rectangle:
    # Previous methods unchanged.

    def __del__(self):
        """
        Destructor method for Rectangle instances.
        Prints a message when an instance is deleted.
        """
        print("Bye rectangle...")
