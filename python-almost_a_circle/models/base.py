#!/usr/bin/python3
""" Base """
import json


class Base:
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ function init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method return json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
