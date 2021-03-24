#!/usr/bin/python3
"""A function that prints x elements of a list from 0-main.py
"""
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for i in my_list:
            if y < x:
                print("{}".format(i), end="")
                y += 1
    except (ValueError, TypeError):
        pass
    print()
    return (y)
