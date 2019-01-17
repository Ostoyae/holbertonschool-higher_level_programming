#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class
    This is the class for the Rectangle Module
    """

    def __init__(self, width, height):
	"""creates Rectangle object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
    
    def area(self):
        """Function that return area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returs a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
