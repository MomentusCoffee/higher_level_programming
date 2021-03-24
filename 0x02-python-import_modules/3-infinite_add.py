#!/usr/bin/python3
"""A program that prints the result of the addition of all arguments
"""
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    sum = 0
    for i in range(1, len):
        sum += int(sys.argv[i])
    print("{}".format(sum))
