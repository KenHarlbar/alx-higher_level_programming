#!/usr/bin/python3
""" File operation module - 0 """


def read_file(filename=""):
    """ function that reads a text file (UTF8)
    and prints it to stdout

    Args:
        filename: name of file

    Return:
        nothing
    """
    if filename:
        with open(filename, mode='r', encoding='UTF-8') as f:
            print(f.read(), end='')
