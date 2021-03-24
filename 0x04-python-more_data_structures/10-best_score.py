#!/usr/bin/python3
"""A function that returns a key with the biggest integer value from 10-main.py
"""
def best_score(a_dictionary):
    try:
        if a_dictionary:
            return (max(a_dictionary, key=lambda v: a_dictionary[v]))
    except ValueError:
        return (None)
