#!/usr/bin/python3
"""Reads file encoded in UTF-8
"""

def read_file(filename=""):
    """
    Returns:
        Text encoded in UTF-8
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
