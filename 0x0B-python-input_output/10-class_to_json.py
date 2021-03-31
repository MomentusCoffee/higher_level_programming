#!/usr/bin/python3
"""
Dictionary description with simple data structure for JSON


"""


def class_to_json(obj):
    """
    Args:
        obj: serilized object of JSON

    Returns:
        Dictionary description with simple data structure for JSON
    """
    return (obj.__dict__)
