#!/usr/bin/python3
"""A class Rectangle that defines a rectangle from 1-main.py
"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initiates parameters of rectangle

        Args:
            width(int): constructs width of rectangle
            height(int): constructs height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property getter/setter

        Used to get/set the width of rectangle

        Args:
            width(int): width of rectangle

        Returns:
            The value of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property getter

        Used to get the height of rectangle

        Args:
            height(int): height of rectangle

        Returns:
            The value of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
