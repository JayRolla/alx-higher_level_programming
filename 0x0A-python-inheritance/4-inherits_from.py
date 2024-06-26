#!/usr/bin/python3
"""Inherits from Module"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class

    Args:
        obj: The object to check
        a_class: The specified class

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
