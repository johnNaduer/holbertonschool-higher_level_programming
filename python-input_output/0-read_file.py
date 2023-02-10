#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """
    This function reads a text file and prints its contents to the standard
    output.

    Args:
    filename (str): The name of the file to be read. The default value is an
    empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding ='utf-8') as file:
        """
        Open the file specified in the 'filename' argument with 'r' mode 
        (read mode)
        and specify the encoding as 'utf-8'. The with statement is used to ensure
        that the file is properly closed after the contents have been read.
        """
        file_contents = file.read()
        print(file_contents,end="")
