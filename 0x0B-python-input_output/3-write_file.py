#!/usr/bin/python3
"""
Writes a string to text file encoded in UTF-8
and returns the number of characters written


"""


def write_file(filename="", text=""):
    """
    Writes string to text file

    Args:
        filename: text file to be written in
        text: text to be added to filename

    Returns:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
