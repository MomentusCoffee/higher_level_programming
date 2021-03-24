#!/usr/bin/python3
"""A function that prints a text with 2 new lines after each of these characters: ., ? from 5-main.py
Usage: ./5-main.py
Edge Cases: python3 -m doctest -v ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Prints 2 newlines after .:?

    Args:
        text: text file to be read and parsed

    Return: new lines after .?:
    """
    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError('text must be a string')
    text = text.replace(". ", ".")
    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    for i in text:
        if i == "." or i == "?" or i == ":":
                print("{}\n".format(i))
        else:
            print(i, end="")
