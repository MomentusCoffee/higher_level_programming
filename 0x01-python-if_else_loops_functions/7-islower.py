#!/usr/bin/python3
"""A function that checks for lowercase and uppercase letters based on ASCII value
"""
def islower(c):
        if ord(c) in range(ord('a'), ord('z')):
                return True
        else:
                return False
