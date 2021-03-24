#!/usr/bin/python3
"""A function that prints all integers of a list, in reverse order from 3-main.py
"""
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for i in range(len(my_list) -1, -1, -1):
            print("{:d}".format(my_list[i]))

if __name__ == "__main__":
    print_reversed_list_integer()
