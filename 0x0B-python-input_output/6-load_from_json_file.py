#!/usr/bin/python3
""" File operations module - 6, including json """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”

    Args:
        filename: json file

    Return: object representation of json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
