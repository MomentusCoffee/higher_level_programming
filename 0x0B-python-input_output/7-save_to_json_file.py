#!/usr/bin/python3
"""
Writes an object to text file using JSON representation


"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to text file

    Args:
        my_obj: object to be written to filename
        filename: file to have object write to
    """
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
