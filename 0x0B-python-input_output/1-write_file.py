#!/usr/bin/python3
""" File operations Module - 1 """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: name of file
        text: text to be written into file

    Return:
        length of text
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
