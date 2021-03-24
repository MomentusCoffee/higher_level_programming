#!/usr/bin/python3
"""A function that adds 2 tuples from 7-main.py
"""
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if len(a) == 0:
        a = (0, 0)
    if len(a) == 1:
        a = (a[0], 0)
    if len(b) == 0:
        b = (0, 0)
    if len(b) == 1:
        b = (b[0], 0)
    return (a[0] + b[0], a[1] + b[1])

if __name__ == "__main__":
    add_tuple()
