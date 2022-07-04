#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """function to check all available \
        attributes and methods of an object

    Args:
        obj: object

    Return:
        all available attributes and methods
    """
    return dir(obj)
