#!/usr/bin/python3
""" File operations module - 5, including json """
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object (data structure)
        filename: name of file

    Return:
        nothing
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
