#!/usr/bin/python3
"""Module doc for BaseGeometry"""


class BaseGeometry:

    def area(self):
        """unimplmente warning"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value
        value must alway be a integer > 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
