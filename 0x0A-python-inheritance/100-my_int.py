#!/usr/bin/python3
"""
Inverts == and != operations


"""


class MyInt(int):
    """
    Creates MyInt
    """
    def __init__(self, value):
        """
        Initiates values for inverting

        Args:
            value: int to be inverted
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.__value = value

    def __eq__(self, num):
        """
        Converts == to != operation

        Args:
            num: number to compare to !=
        """
        return (self.__value != num)

    def __ne__(self, num):
        """
        Converts != to == operation

        Args:
            num: number to compare to ==
        """
        return (self.__value == num)

    def __str__(self):
        """
        Returns:
            Inverted values
        """
        return (str(self.__value))
