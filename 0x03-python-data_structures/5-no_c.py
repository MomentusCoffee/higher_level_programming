#!/usr/bin/python3
"""A function that removes all characters c and C from a string in 5-main.py
"""
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return (new_string)

if __name__ == "__main__":
    no_c()
