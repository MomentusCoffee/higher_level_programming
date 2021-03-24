#!/usr/bin/python3
"""A function that prints an integer with "{:d}".format() from 1-main.py
"""
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
