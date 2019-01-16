#!/usr/bin/python3


def inherits_from(obj, a_class):
    """check if obj is instance and inherited of a_class"""
    return not issubclass(a_class, type(obj))
