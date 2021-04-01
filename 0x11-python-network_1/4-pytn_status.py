#!/usr/bin/python3
"""fetches https://en.wikipedia.org/wiki/Main_Page
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
    print("Body response:\n\t- type: {}\n\t- content:\
 {}".format(type(r.text), r.text))
