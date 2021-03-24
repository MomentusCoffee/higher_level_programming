#!/usr/bin/python3
"""A function that prints the first x elements of a list and only integers from 2-main.py
"""
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except (ValueError, TypeError):
            continue
    print()
    return (y)
