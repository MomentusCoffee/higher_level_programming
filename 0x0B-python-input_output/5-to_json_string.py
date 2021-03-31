#!/usr/bin/python3
"""
Returns JSON representation of an object


"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object

    Args:
        my_obj: object to be represented in JSON

    Returns:
        JSON represenation of object
    """
    return (json.dumps(my_obj))
