#!/usr/bin/python3
"""Defines a function that saves an object to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    new_json = json.dumps(my_obj)
    with open(filename, 'w',encoding='utf8') as file:
        file.write(new_json)
