#!/usr/bin/python3

def number_of_lines(filename=""):
    """ Function that count the number of lines
    """
    i = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            i += 1
    return i
