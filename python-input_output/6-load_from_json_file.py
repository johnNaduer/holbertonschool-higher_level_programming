#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Open the file specified by "filename" in read mode"""
    with open(filename, 'r') as file:
        read_file = file.read()
        new_data = json.loads(read_file)
        return (new_data)
