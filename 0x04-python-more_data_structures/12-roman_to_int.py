#!/usr/bin/python3
"""A function that converts a Roman numeral to an integer from 12-main.py
"""
def roman_to_int(roman_string):
    ro_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_list = []
    result = 0
    try:
        new_list = [ro_dict.get(x) for x in roman_string if x in ro_dict]
        for i, v in enumerate(new_list):
            if i < len(new_list) - 1:
                if v < new_list[i + 1]:
                    result -= v
                else:
                    result += v
            else:
                result += v
        return (result)
    except (TypeError, IndexError, ValueError):
        return (0)
