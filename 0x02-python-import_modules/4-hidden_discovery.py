#!/usr/bin/python3
"""A program that prints all the names defined by the compiled module hidden_4.pyc
"""
if __name__ == "__main__":
    import hidden_4
    for names in dir(hidden_4):
        if not names.startswith("__"):
            print("{}".format(names))
