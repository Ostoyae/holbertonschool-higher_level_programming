#!/usr/bin/python3

def write_file(filename="", text=""):
    """ Function that write to a file"""
    with open(filename, mode='w') as f:
        return f.write(text)
