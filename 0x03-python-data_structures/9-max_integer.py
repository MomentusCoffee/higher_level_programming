#!/usr/bin/python3
"""A function that finds the biggest integer of a list from 9-main.py
"""
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return (max)

if __name__ == "__main__":
    max_integer()
