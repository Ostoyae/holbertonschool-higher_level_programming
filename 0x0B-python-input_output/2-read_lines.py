#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):
    """ Function that read n lines"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines<= 0:
            print(f.read())
        for i in range(nb_lines):
            print(f.readline(), end="")
