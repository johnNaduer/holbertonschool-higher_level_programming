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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """metohd JSON string to file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        with open(filename, mode='w') as file:
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string'"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        else:
            dict_list = cls.from_json_string(json_string)
            instances = []
            for dictionary in dict_list:
                instance = cls.create(**dictionary)
                instances.append(instance)
            return instances
