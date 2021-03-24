#!/usr/bin/python3
"""a function that retrieves an element from 1-main.py
"""
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return (None)
    else:
        return (my_list[idx])

if __name__ == "__main__":
    element_at()
