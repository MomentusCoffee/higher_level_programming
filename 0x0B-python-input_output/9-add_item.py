#!/usr/bin/python3
"""
Adds all arguments to a Python list


"""

import os
import sys
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"
lst = []

if not os.path.exists(filename):
    save_to_json_file(lst, filename)
if os.path.exists(filename):
    lst = load_from_json_file(filename)
lst.extend(sys.argv[1:])
save_to_json_file(lst, filename)
