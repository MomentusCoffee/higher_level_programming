#!/usr/bin/python3
"""BaseGeometry that raises error when getting area from 6-main.py
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """
        raises Error messege

        Returns:
            Exception Error messege
        """
        raise Exception("area() is not implemented")
