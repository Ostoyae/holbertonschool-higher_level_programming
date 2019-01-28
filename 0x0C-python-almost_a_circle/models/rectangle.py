#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class for modules rectangle
    """

    __size_names = ["width", "height", "size"]
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
    def validate(attr, value):
        """ This function will will check if the value used for a specific
        attribute is valide
        """

        all_attr = Rectangle.__size_names + Rectangle.__pos_names + ["id"]
        # if attr is not 'id': uncomment this if id can anything
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(attr))

        if attr in Rectangle.__size_names and value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        elif attr in Rectangle.__pos_names and not value >= 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif attr not in all_attr:
            raise TypeError(
                "{} is not an attrbute of this object".format(attr))

    def update(self, *args, **kwargs):
        """ Update the values visa ordered list or key/word pair

        args order - id, width, height, x, y

        >>> rec = Rectangle(1, 1, 5, 5, 1337)
        >>> str(rec)
        '[Rectangle] (1337) 5/5 - 1/1'
        >>> rec.update(42, 10, 5, 25, 50)
        >>> str(rec)
        '[Rectangle] (42) 25/50 - 10/5'
        >>> rec.update(id=1337)
        >>> str(rec)
        '[Rectangle] (1337) 25/50 - 10/5'
        >>>
        """
        attr = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                Rectangle.validate(k, v)
                setattr(self, k, v)

    def area(self):
        """ Return the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """ Print out a rectangle to the prompt

        >>> rec = Rectangle(5, 5, 1, 2)
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

    def __str__(self):
        """ return object details as str
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def to_dictionary(self):
        """ Return dictionary representation of object
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
