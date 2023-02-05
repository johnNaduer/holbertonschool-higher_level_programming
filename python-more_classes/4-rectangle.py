#!/usr/bin/python3
"""Contains the rectangle class"""


class Rectangle:
    """A rectangle class"""	
    def __init__(self, width=0, height=0):
        """Initilizes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self._width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """height property"""
        return self._height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns area of a rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns rectangle str"""    
        if self._width == 0 or self._height == 0:
            return ""
        rectangle = ""
        for i in range(self._height):
            rectangle += "#" * self._width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Returns repr of the rectangle"""
        return f"Rectangle({self._width}, {self._height})"
