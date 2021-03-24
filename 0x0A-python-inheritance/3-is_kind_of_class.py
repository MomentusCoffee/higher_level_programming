#!/usr/bin/python3
"""a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False from 3-main.py
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is of a specified class

    Args:
        obj: object to be compared to a_class
        a_class: a specified class to check obj against

    Returns:
        True if obj matches class
        False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
