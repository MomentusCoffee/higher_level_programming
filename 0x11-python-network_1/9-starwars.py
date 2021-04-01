#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/people/?search={}"
                     .format(sys.argv[1]))
    load = r.json()
    print("Number of results: {}".format(load['count']))
    for i in load['results']:
        print(i['name'])
