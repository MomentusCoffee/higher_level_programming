#!/usr/bin/python3
"""A program that prints all possible different combinations of two digits
"""
for i in range(1, 100):
    ten = i / 10
    one = i % 10
    if one > ten:
        if i != 89:
            print("{:02d}". format(i), end=", ")
        else:
            print("{:02d}".format(i))
