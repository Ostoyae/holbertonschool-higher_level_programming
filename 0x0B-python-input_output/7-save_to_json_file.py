#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON
    representation
    """
    j_obj = json.JSONEncoder().encode(my_obj)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(j_obj)
