#!/usr/bin/python3
"""A class Square that defines a square from 4-main.py
"""


class Square:
    """
    Defines a Square
    """
    def __init__(self, size=0):
        """
        Initializes size of square

        """
        self.__size = size

    @property
    def size(self):
        """
        Property getter

        Used to get the size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Property setter

        Used to set the size of square

        Args:
            value(int): size of square
                - size is a private instance
                - size must be an integer
                - size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Gets the area of square

        Returns:
            area of square
        """
        return (self.__size * self.__size)
