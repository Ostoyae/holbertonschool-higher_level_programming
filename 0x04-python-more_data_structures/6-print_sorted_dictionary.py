#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = list(a_dictionary.keys())
    ls.sort()
    for k in ls:
        print("{}: {}".format(k, a_dictionary.get(k)))
