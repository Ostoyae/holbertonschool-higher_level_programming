#!/usr/bin/python3
"""Define class Base"""
import json
import csv


class Base():
    """Class Base 
    
    class for modules base.

    This is the base class for all other class to be built on top of
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Creates an ID"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def reset():
        """ Resets private var __nb_objects to 0
        used for testing only
        """
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert object/dic into json strings
        """
        dictionary = []
        if not list_dictionaries:
            return list()
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

    @staticmethod
    def from_json_string(json_string):
        """ Creates Dictionaries from a json string
        """
        if not json_string:
            return list()
        return json.JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create new instance from a dictionary
        """
        if cls.__name__ == "Square":
            obj = cls(1, 1, 1, 42)
        else:
            obj = cls(1, 1, 1, 1, 42)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ load a json file and create instances
        else if file doesn't exist return a empty
        list
        """
        ls_dict = []
        objs = []
        try:
            with open("{}.json".format(cls.__name__)) as f:
                ls_dict = cls.from_json_string(f.read())
                for ele in ls_dict:
                    objs.append(cls.create(**ele))
                f.close()
        finally:
            return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save out a list of objects as a csv file
        """
        with open(cls.__name__ + ".csv", "w") as f:
            for idx, i in enumerate(list_objs):
                d = i.to_dictionary()
                if idx == 0:
                    w = csv.DictWriter(f, fieldnames=d.keys())
                    w.writeheader()
                w.writerow(d)
            f.close()

    @classmethod
    def load_from_file_csv(cls):
        """ Loads up ojbect instances from a csv file
        """
        objs = list()
        with open(cls.__name__ + ".csv", "r") as f:
            csv_read = csv.DictReader(f)
            for row in csv_read:
                row = {k: int(v) for k, v in row.items()}
                objs.append(cls.create(**row))
            f.close()
        return objs
