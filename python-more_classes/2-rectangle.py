#!/usr/bin/python3
"""Contains the rectangle class"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Rectangle initializor"""
        self.__height = height
        self.__width = width

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """Width property function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return value

    @property
    def height(self):
        """Height property function"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
        return value

    def area(self):
        """function area"""
        return self.__height * self.__width

    def perimeter(self):
        """function perimeter"""
        return (self.__height  + self.__width)*2
