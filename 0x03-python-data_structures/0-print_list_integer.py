#!/usr/bin/python3
"""A function that prints all integers of a list from 0-main.py
"""
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

if __name__ == "__main__":
    print_list_integer()
