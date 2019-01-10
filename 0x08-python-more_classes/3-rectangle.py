#!/usr/bin/python3
"""Module of Rectangle """


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """create a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for property width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the property height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Function caculates the area

        Returns the area as an int
        """
        return self.width * self.height

    def perimeter(self):
        """
        Function caculates the perimeter

        Returns the perimeter as an int
        """
        return (self.width + self.height) * 2

    def __str__(self):
        """
        This method will generate a string of the rectangle.

        Returns a String
        """
        rec = "\n"
        if self.width is not 0 or self.height is not 0:
            rec = ""
            for row in range(self.height):
                rec = rec + ("#" * self.width)
                if row < self.height - 1:
                    rec = rec + "\n"
        return rec
