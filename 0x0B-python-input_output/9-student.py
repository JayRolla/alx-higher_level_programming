#!/usr/bin/python3
"""
Defines a class Student that represents a student with first_name, last_name, and age.
"""

class Student:
    """A student with first_name, last_name, and age attributes."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return self.__dict__
