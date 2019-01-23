#!/usr/bin/python3
import json

class Base():
    """ Base class for modules base.
    """
    
    __nb_objects = 0;


    def __init__(self, id=None):
        """ Creates an ID"""
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert object/dic into json strings
        """
        dictionary = []
        if not list_dictionaries:
            return []
        for ele in list_dictionaries:
            if isinstance(ele, dict):
                dictionary.append(ele)
            else:
                dictionary.append(ele.to_dictionary())

        return json.JSONEncoder().encode(dictionary)

    @classmethod
    def save_to_file(cls, list_objc):
        """ save a json file"""
        with open("{}.json".format(cls.__name__), "w") as f:
            json_str = cls.to_json_string(list_objc)
            f.write(json_str)
        
