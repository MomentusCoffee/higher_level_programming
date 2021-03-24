#!/usr/bin/python3
"""A function that replaces an element in a list at a specific
position without modifying the original list from 4-main.py
"""
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        new_list[idx] = element
        return (new_list)

if __name__ == "__main__":
    new_in_list()
