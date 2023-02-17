#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object."""
        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.size = size

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")      
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] (<id>) <x>/<y> - <size>'.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
