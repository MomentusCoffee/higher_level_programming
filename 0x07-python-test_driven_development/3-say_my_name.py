#!/usr/bin/python3
"""A function that prints My name is <first name> <last name> from 3-main.py
Usage: ./3-main.py
Edge Cases: python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name

    Args:
        first_name: takes a string argument
        last_name: takes a string argument

    Return: 2 string arguments

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
