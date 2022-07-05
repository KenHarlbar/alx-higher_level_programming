#!/usr/bin/python3
""" File operations module - 4, including json """
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: string

    Return:
        object representation of my_str
    """
    return json.loads(my_str)
