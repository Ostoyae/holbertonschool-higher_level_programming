#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class for this module
    """

    def __init__(self, size):
        """create Square object"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
