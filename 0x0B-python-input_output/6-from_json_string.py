#!/usr/bin/python3
import json

def from_json_string(my_string):
    """function that returns an object (Python data structure) represented by a
    JSON string:
    """
    return json.JSONDecoder().decode(my_string)
