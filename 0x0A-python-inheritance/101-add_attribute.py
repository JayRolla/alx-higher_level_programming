#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class with integer validation."""
    
    def area(self):
        """Placeholder for area computation."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that the 'value' is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
