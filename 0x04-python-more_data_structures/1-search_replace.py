#!/usr/bin/python3
"""A function that replaces all occurrences of an element by another in a new list from 1-main.py
"""
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
    return (new_list)
