#!/usr/bin/python3
"""A function that adds 2 integers from 0-main.py
Usage: ./0-main.py
Edge Cases: python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
"""


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a: requires integer argument
        b: optional integer argument

    Return:
        Sum of int a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
