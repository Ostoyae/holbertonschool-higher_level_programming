#!/use/bin/python3


class Student:
    """ Student Class for the module
    """

    def __init__(self, first_name, last_name, age):
        """ Create a student Object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """  function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an object
        """
        if not attr:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attr}
