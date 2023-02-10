#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """
    Writes the given text to a file with the given filename.

    Parameters:
    filename (str, optional): The name of the file to write. Default
    an empty string.
    text (str, optional): The text to write to the file. Default is an empty
    string.

    Returns:
        int: The length of the text written to the file.
    """
    with open(filename,'w',encoding='utf-8') as file:
        write_filename = file.write(text)
        return len(text)
