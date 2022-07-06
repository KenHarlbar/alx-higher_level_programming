#!/usr/bin/python3
""" File operations module - 8 """


def class_to_json(obj):
    """ function that returns the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object

    Args:
        obj: instance of a class

    Return:
        dictionary description with simple data structure
    """
    result = {}
    if hasattr(obj, '__dict__'):
        result = obj.__dict__.copy()
    return result
