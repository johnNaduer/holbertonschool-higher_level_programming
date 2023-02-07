#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Class Square represents a square object with a size.
    The size of the square must be a non-negative integer.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the class with a given size.
        If size is not specified, it will default to 0.
        :param size: the size of the square, must be a non-negative integer
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is less than 0
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Gets the size of the square.
        :return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        :param value: the new size of the square, must be a non-negative integer
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.
        :return: the area of the square
        """
        return self.__size*self.__size
