#!/usr/bin/python3
"""Defines a function that converts an object to a json string"""
import json

def from_json_string(my_str):
    """Converts an object to a json string"""    
    new_objetc = json.loads(my_str)
    return (new_objetc)
