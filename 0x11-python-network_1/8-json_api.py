#!/usr/bin/python3
"""takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter
    as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    try:
        value = {'q': sys.argv[1]}
    except:
        value = {'q': ""}
    r = requests.post("http://0.0.0.0:5000/search_user", value)
    try:
        load = r.json()
        if len(load) == 0:
            print("No result")
        else:
            print("[{}] {}".format(load['id'], load['name']))
    except:
        print("Not a valid JSON")
