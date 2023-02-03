#!/usr/bin/python3
"""this module containing a function that prints a square"""


def print_square(size):

    """Prints a square made of "#" characters with the given size"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0 :
        raise ValueError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    x = 0
    while x < size:
        y = 0
        while y < size:
            print("#", end="")
            y = y + 1
        print("")
        x = x + 1
