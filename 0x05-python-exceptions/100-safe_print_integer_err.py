#!/usr/bin/python3
"""A function that prints an integer from 100-main.py
"""
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)
