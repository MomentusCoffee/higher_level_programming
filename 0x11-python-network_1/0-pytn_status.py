#!/usr/bin/python3
"""fetches https://en.wikipedia.org/wiki/Main_Page
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page') as r:
        html = r.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content:\
 {}".format(type(html), html, html.decode("utf-8")))
