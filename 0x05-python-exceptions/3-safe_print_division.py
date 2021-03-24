#!/usr/bin/python3
"""A function that divides 2 integers and prints the result from 3-main.py
"""
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
