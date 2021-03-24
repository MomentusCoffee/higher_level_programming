#!/usr/bin/python3
"""A class MyList that inherits from list from 1-main.py
"""


class MyList(list):
    """
    Inherits built-in function list
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print("{}".format(sorted(self)))
