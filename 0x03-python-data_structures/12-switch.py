#!/usr/bin/python3
"""Switches the value of 2 variables
"""
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
