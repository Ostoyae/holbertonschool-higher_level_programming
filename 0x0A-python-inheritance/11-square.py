#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class for the module
    """

    def __init__(self, size):
        """creats Square object"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """return detail on objects area"""
        return "[Square] {}/{}".format(self.__size, self.__size)
