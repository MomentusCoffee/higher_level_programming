#!/usr/bin/python3
"""BaseGeometry that raises error when getting area from 7-main.py
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """
        Raises exception messege

        Returns:
            Exception Error messege
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if objects are of type int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
