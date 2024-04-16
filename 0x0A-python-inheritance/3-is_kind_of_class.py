#!/usr/bin/python3
"""Kind of class Module"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class

    Args:
        obj: The object to check
        a_class: The specified class

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False
    """
    return isinstance(obj, a_class)
