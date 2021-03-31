#!/usr/bin/python3
"""
Reads specific amount of lines in an encoded UTF-8 text file


"""


def read_lines(filename="", nb_lines=0):
    """
    Reads specific amoutn of lines in a text file

    Args:
        filename: text file to be read
        nb_lines: specified number of lines to read

    Returns:
        Lines specified for reading
    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line, word in enumerate(f):
                if line < nb_lines:
                    print(word, end="")
