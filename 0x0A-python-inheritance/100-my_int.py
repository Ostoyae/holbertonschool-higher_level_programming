#!/usr/bin/python3
"""MyInt Module
"""

class MyInt(int):

    def __init__(self, value):
        """create a MyInt obj"""
        self.value = value

    def __eq__(self, other):
        """inverts =="""
        return self.value != other
    
    def __ne__(self, other):
        """invert !="""
        return self.value == other
    
