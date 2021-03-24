#!/usr/bin/python3
"""A function that replaces an element of a list at a specific position from 2-main.py
"""
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)

if __name__ == "__main__":
    replace_in_list()
