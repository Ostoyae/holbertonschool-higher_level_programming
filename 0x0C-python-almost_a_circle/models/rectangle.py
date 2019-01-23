#!/usr/bin/python3
from models.base import Base 


class Rectangle(Base):
    """ Rectangle Class for modules rectangle
    """

    __size_names = ["width", "height"]
    __pos_names = ["x", "y"]
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Create an Rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """ Return width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width attribute"""
        Rectangle.validate("width", value)
        self.__width = value
    
    @property
    def height(self):
        """ Return height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height attribute"""
        Rectangle.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ Return x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Set X attribute"""
        Rectangle.validate("x", value)
        self.__x = value
    
    @property
    def y(self):
        """ Return Y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Set Y attribute """
        Rectangle.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(attr , value):
        """ This function will will check if the value used for a specific
        attribute is valide
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(attr))

        if attr in Rectangle.__size_names and value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        elif attr in Rectangle.__pos_names and not value >= 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif attr not in Rectangle.__size_names + Rectangle.__pos_names:
            raise TypeError("{} is not an attrbute of this object".format(attr))

    def area(self):
        """ Return the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """ Print out a rectangle to the prompt

        >>> rec = Rectangle(5, 5, 2, 0)
        >>> rec.display()
        <BLANKLINE>
        <BLANKLINE>
        #####
        #####
        #####
        #####
        #####
        >>>
        """
        print(end="\n" * self.y)
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)


if __name__ == "__main__":
    import doctest
    doctest.testmod()