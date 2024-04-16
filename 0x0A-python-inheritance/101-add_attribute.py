#!/usr/bin/python3
"""
This module defines a function add_attribute that adds a new attribute
to an object if it's possible.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.
    Raises a TypeError if the attribute cannot be added.
    """
    if '__dict__' in dir(obj) or '__slots__' in dir(obj):
        if hasattr(obj, '__slots__') and not hasattr(obj, attr_name):
            raise TypeError("can't add new attribute")
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
