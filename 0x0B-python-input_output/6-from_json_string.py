#!/usr/bin/python3
"""
Returns an object represented by a JSON string


"""
import json


def from_json_string(my_str):
    """
    Object represented by JSON string

    Args:
        my_str: string to be represented by JSON

    Returns:
        JSON string
    """
    return (json.loads(my_str))
