#!/usr/bin/python3
"""A function that prints a dictionary by ordered keys from 6-main.py
"""
def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
