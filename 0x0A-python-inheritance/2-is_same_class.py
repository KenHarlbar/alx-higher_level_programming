#!/usr/bin/python3
"""is_same_class Module"""


def is_same_class(obj, a_class):
    """method for comparing type of an instance to a class

    Args:
        obj: instance / object
        a_class: class

    Return:
        True: if type of obj is a_class
        False: if otherwise
    """
    return type(obj) == a_class
