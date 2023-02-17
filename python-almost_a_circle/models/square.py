#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] (<id>) <x>/<y> - <size>'.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
