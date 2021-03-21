#!/usr/bin/python3
"""a program that prints the alphabet based on ASCII values except for letters q and e
"""
for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print("{}".format(chr(i)), end='')
