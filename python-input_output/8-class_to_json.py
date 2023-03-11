#!/usr/bin/python3
""" function that returns the dictionary description with simple
data structure
"""


def class_to_json(obj):
    """ class return to dict """

    data = obj.__dict__
    return data;
