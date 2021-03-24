#!/usr/bin/python3
"""A function that returns a set of all elements present in only one set from 4-main.py
"""
def only_diff_elements(set_1, set_2):
    return {x for x in set_1 ^ set_2}
