#!/usr/bin/python3
"""Defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class for this module
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Creates Square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return deatil on Square object as string

        >>> sqr = Square(5, 2, 4, 1337)
        >>> str(sqr)
        '[Square] (1337) 2/4 - 5'
        >>>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate("size", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                self.validate(attr[i], args[i])
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                self.validate(k, v)
                setattr(self, k, v)

    def to_dictionary(self):
        """ Return dictionary representation of object
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
