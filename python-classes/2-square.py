#!/usr/bin/python3
"""
Module square

This module contains the Square class, which defines a square object.

Classes:
    Square: Defines a square object with size attribute.

"""


class Square:
    """
    Square class.

    Defines a square object with size attribute.

    Attributes:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size =0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
