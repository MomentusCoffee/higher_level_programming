#!/usr/bin/python3
"""A function that prints a square with the character # from 4-main.py
Usage: ./4-main.py
Edge Cases: python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """
    Prints a square

    Args:
        size: size of int square

    Returns: square of #

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        print('#' * size)
