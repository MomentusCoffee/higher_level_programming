#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry from 8-main.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Creates Rectangle
    """
    def __init__(self, width, height):
        """
        Initiates objects for creating a Rectangle

        Args:
            width: width of Rectangle
            height: height of Rectangle

        Notes:
            width and height must be positive
            integers, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
