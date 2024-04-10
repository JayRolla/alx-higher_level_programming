#!/usr/bin/python3
"""
Includes a __repr__ method to enable recreation of a Rectangle instance from its string representation.
"""
class Rectangle:
    # Previous methods unchanged.

    def __repr__(self):
        """
        Returns a string representation of the Rectangle that can recreate a new instance by using eval().
        Returns:
            String representation of the rectangle that can be used by eval() to create a new instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
