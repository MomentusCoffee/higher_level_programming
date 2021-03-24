#!/usr/bin/python3
"""Module to find the max integer in a list from 6-main.py
Usage: test/./6-main.py
Unitest: python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
