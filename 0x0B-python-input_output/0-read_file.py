#!/usr/bin/python3


def read_file(filename=""):
    """ Function that read and print out
    contents of a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
