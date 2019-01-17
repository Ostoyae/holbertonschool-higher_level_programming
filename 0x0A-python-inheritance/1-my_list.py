#!/usr/bin/python3
"""MyList modules
"""

class MyList(list):
    """MyList class
    """

    def print_sorted(self):
    """ function that print a sorted list"""
    s = self.copy()
    s.sort()
    print(s)
