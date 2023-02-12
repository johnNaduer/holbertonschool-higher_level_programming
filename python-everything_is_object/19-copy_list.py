#!/usr/bin/python3
""" function def copy_list(a_list): that returns a copy of a list """


def copy_list(a_list):
    """ function that return copy a_list """
    new_list = []
    i = 0
    while i < len(a_list):
        new_list.append(a_list[i])
        i = i + 1
    return (new_list)
