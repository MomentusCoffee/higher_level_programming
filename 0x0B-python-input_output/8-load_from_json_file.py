#!/usr/bin/python3
"""
Creates an object from a JSON file


"""
import json


def load_from_json_file(filename):
    """
    Creates an object

    Args:
        filename: file in which object will be created from
    """
    with open(filename, mode="r") as f:
        return (json.load(f))
