#!/usr/bin/python3
"""A function that divides element by element 2 lists from 4-main.py
"""
def list_division(my_list_1, my_list_2, list_length):
    llen = 0
    new = []
    for i in range(list_length):
        try:
            llen = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            llen = 0
        except ZeroDivisionError:
            print("division by 0")
            llen = 0
        except IndexError:
            print("out of range")
            llen = 0
        finally:
            new.append(llen)
    return (new)
