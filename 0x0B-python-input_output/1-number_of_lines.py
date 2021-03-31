#!/usr/bin/python3
"""
Returns number of lines of a text file


"""


def number_of_lines(filename=""):
    """
    Counts number of lines in text file

    Args:
        filename: text file to be read

    Returns:
        Number of lines in text file
    """
    with open(filename) as f:
        result = 0
        for line in f:
            result += 1
        return (result)
