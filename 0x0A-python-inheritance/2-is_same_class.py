#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance of the specified class;
otherwise False from 2-main.py
"""


def is_same_class(obj, a_class):
    """
    Checks if object is the specified class

    Args:
        obj: object to be compared to class
        a_class: class used to check against obj

    Returns:
        True if same
        False if different
    """
    if obj.__class__ is a_class:
        return (True)
    else:
        return (False)
