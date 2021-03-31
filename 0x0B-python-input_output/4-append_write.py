#!/usr/bin/python3
"""
Appends text to file encoded in UTF-8


"""


def append_write(filename="", text=""):
    """
    Appends text to file

    Args:
        filename: file to append text to
        text: text to be appended into filename
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
