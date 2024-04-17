#!/usr/bin/python3
"""
Defines a class Student that can serialize to JSON and reload from JSON.
"""

class Student:
    """A student who can be serialized to JSON and reloaded."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with ones from the json."""
        for key, value in json.items():
            setattr(self, key, value)
