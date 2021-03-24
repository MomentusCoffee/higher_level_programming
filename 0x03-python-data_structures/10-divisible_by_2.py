#!/usr/bin/python3
"""A function that finds all multiples of 2 in a list from 10-main.py
"""
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)

if __name__ == "__main__":
    divisible_by_2()
