#!/usr/bin/python3
"""A function that returns the list of available attributes and methods of an object from 0-main.py
"""


def lookup(obj):
    """
    The built-in function dir() is used to find out
    which names a module defines.

    Args:
        obj: argument being used to lookup attribute and methods

    Returns:
        a sorted list in argument obj
    """
    return (dir(obj))
