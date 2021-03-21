#!/usr/bin/python3
"""A program that prints the alphabet based on ASCII value
"""
for i in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(i)), end='')
