#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
    displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        if r.raise_for_status() is None:
            print(r.text)
    except:
        print("Error code: {}".format(r.status_code))
