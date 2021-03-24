#!/usr/bin/python3
"""A function that returns the weighted average of all integers tuple from 100-main.py
"""
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(tuple(a * b for a, b in my_list))/sum(x[1] for x in my_list)
