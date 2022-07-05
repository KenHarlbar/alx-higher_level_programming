#!/usr/bin/python3
""" File operations module - 3. Includes json """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an
    object (string)

    Args:
        my_obj: obj

    Return:
        json representation of an object
    """
    return json.dumps(my_obj)
