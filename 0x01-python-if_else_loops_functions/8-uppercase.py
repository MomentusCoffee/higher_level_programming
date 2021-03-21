#!/usr/bin/python3
"""A function that prints a string in uppercase
"""
def uppercase(str):
        for i in str:
                if ord(i) in range(ord('a'), ord('z')):
                        x = chr(ord(i) - 32)
                else:
                        x = chr(ord(i))
                print("{}".format(chr(ord(x))), end='')
        print()
