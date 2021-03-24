#!/usr/bin/python3
"""A function that deletes a key in a dictionary from 8-main.py
"""
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return (a_dictionary)
