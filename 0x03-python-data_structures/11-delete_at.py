#!/usr/bin/python3
"""A function that deletes the item at a specific position in a list from 11-main.py
"""
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)

if __name__ == "__main__":
    delete_at()
