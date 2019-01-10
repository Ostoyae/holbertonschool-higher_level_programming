#!/usr/bin/python3
"""Module of Rectangle """


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """create a new rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width is 0 or self.height is 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        This method will generate a string of the rectangle.

        Returns a String
        """
        rec = ""
        if self.width is not 0 and self.height is not 0:
            for row in range(self.height):
                rec = rec + (str(self.print_symbol) * self.width)
                if row < self.height - 1:
                    rec = rec + "\n"
        return rec

    def __repr__(self):
        """
        This method returns a reprsentation of the class
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        This function will reduce the number_of_instances by 1
        and notify the user when a instance is deleted

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        This function will compare two instance to each other

        Return True is rect_1 is Large or equal to rect_2 else False
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1.area()
        else:
            return rect_2.area()
