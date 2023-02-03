#!/usr/bin/python3
"""
Module Documentation for Square class

The Square module contains a class called Square that represents a square object with a size attribute.
The class has a __init__ method that initializes the size attribute of the square object and
raises TypeError and ValueError exceptions if the size is not an integer or is less than 0, respectively.
The class also has an area method that calculates and returns the area of the square object.
"""

class Square:
    """
    Square Class Documentation

    This class represents a Square object with a size attribute.
    The class has a __init__ method that initializes the size attribute of the square object and
    raises TypeError and ValueError exceptions if the size is not an integer or is less than 0, respectively.
    The class also has an area method that calculates and returns the area of the square object.
    """
    def __init__(self, size =0):
        """
        __init__ method Documentation

        The __init__ method initializes the size attribute of the square object and
        raises TypeError and ValueError exceptions if the size is not an integer or is less than 0, respectively.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        area method Documentation

        The area method calculates and returns the area of the square object.
        """
        Area = self.__size*self.__size
        return (Area)
