#!/usr/bin/python3
""" File operations module - 2 """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added.

    Args:
        filename: name of file
        text: string to be appended

    Return:
        number of characters added
    """
    with open(filename, 'a') as f:
        f.write(text)
        return len(text)
