#!/usr/bin/python3
"""Module containing a function that separates sentences"""


def text_indentation(text):
    """Adds a newline character after each '.', '?' and ':' in the given text"""
    if type(text) is not str:
         raise TypeError("text must be a string")
    x = 0
    inicio = 0
    while x < len(text):
        if text[x]== '.' or text[x]== '?' or text[x] ==':':
            string = text[inicio:x+1]
            inicio = x + 2
            print(string)
            print("")
        x = x + 1
