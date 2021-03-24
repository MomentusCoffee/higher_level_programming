#!/usr/bin/python3
"""A function that returns a new dictionary with all values multiplied by 2 from 9-main.py
"""
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return (new_dict)
