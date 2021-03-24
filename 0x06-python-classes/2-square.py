#!/usr/bin/python3
"""A class Square that defines a square from 2-main.py
"""


class Square:
    """
    Defines a Square
    """
    def __init__(self, size=0):
        """
        Initializes size of square

        Args:
            size: size of square
                - size is a private instance
                - size must be an integer
                - size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
