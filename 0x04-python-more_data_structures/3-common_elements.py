#!/usr/bin/python3
"""A function that returns a set of common elements in two sets from 3-main.py
"""
def common_elements(set_1, set_2):
    return {x for x in set_1 if x in set_2}
