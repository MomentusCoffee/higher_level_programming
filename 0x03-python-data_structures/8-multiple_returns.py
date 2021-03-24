#!/usr/bin/python3
"""A function that returns a tuple with the length of a string and its first character
from 8-main.py
"""
def multiple_returns(sentence):
    if sentence is not None:
        if len(sentence) > 0:
            return (len(sentence), sentence[0])
        else:
            return (len(sentence), None)

if __name__ == "__main__":
    multiple_returns()
