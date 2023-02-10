#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8) and
returns the number of characters added"""


def append_write(filename="", text=""):
    """
    This function takes a filename and text as input, and writes the text
    to the file specified by the filename.

    Parameters:
    filename (str): The name of the file to write to. Defaults to an
    empty string.
    text (str): The text to write to the file. Defaults to an empty string.

    Returns:
    int: The length of the text written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file_append = file.write(text)
        return len(text)
