#!/usr/bin/python3
"""
Creates a Square


"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates a Square
    """
    def __init__(self, size):
        """
        Initiates objects for creating a square

        Args:
            size: size of square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
