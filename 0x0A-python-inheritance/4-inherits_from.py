#!/usr/bin/python3
"""A function that returns True if the object is an
instance of a class that inherited (directly or
indirectly) from the specified class; otherwise False from 4-main.py
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of specified class

    Args:
        obj: object to be compared to a_class
        a_class: class to be check against object

    Returns:
        True if it is an instance of specified class
        False if not
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
