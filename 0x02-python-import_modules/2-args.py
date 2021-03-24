#!/usr/bin/python3
"""A program that prints the number of and the list of its arguments
"""
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 1:
        print("{}".format("0 arguments."))
    elif len == 2:
        print("{}".format("1 argument:"))
    else:
        print("{:d} arguments:".format(len - 1))
    for i in range(1, len):
        print("{:d}: {}".format(i, sys.argv[i]))
