#!/usr/bin/python3
"""
Defines a class Student that defines a student by first_name, last_name, and age.
Can serialize student to JSON, optionally filtering by attributes.
"""

class Student:
    """A student with attributes that can be serialized to JSON."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, returns only those attributes included in the list.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
