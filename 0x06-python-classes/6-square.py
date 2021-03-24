#!/usr/bin/python3
"""A class Square that defines a square from 6-main.py
"""


class Square:
    """
    Defines a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes:
            - size of square
            - position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Property getter

        Used to get position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Property setter

        Used to set the position of square

        Args:
            value(int): position of square
                - position is a private instance
                - position must be tuple
                - position must 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Gets the area of square

        Returns:
            area of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints area of square and fills it with #

        Note:
            - if size == 0, print newline
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
