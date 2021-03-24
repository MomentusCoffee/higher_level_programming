#!/usr/bin/python3
"""A class Rectangle that defines a rectangle from 7-main.py
"""


class Rectangle:
    """
    Defines a rectangle

    Args:
        number_of_instances: Counts number of instances created
        print_symbol: prints # to represent string
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initiates parameters of rectangle

        Args:
            width(int): constructs width of rectangle
            height(int): constructs height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Gets the area of rectangle

        Returns:
            area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Gets the perimeter of rectangle

        Returns
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.width) + (self.height + self.height))

    def __str__(self):
        """
        Returns rectangle represented by #
        """
        if self.width == 0 or self.height == 0:
            return("")
        return ("\n".join((str(self.print_symbol) * self.width)
                for i in range(self.height)))

    def __repr__(self):
        """
        Returns a string representation of rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints message when rectangle is deleted
        """
        print("{}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1
