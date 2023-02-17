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

    def update(self, *args, **kwargs):
        """method return *args and **kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        elif args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
