#!/usr/bin/python3
""" class of name BaseGeometry"""


class BaseGeometry:
    """super class for geometry objects"""
	
    def area(self):
        """Returns area of geometry object if implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether values is an integer"""
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
