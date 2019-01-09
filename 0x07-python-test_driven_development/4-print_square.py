#!/usr/bin/python3
"""Doc"""


def print_square(size):
    """Function that print a square in to the prompte"""
    if size == 0:
        print()
        return
    if size < 0 and isinstance(size, int):
        raise ValueError("size must be >= 0")
    elif size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    s = int(size)
    for r in range(s):
        print("#" * s)
