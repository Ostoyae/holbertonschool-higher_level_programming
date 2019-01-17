#!/usr/bin/python3

def append_write(filename="", text=""):
    """ function that append to a file""" 
    with open(filename, mode='a') as f:
        return f.write(text)
