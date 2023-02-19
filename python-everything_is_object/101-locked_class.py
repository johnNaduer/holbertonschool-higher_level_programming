#!/usr/bin/python3
""" the class LockedClass is create """


class LockedClass:
    """class that create attribute first_name """
    def __setattr__(self, attr, val):
        if attr != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{attr}'")
        self.__dict__[attr] = val
