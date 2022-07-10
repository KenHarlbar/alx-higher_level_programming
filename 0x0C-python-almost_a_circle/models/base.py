#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes class Base """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Method that returns the JSON string representation
        of list_dictionaries'''

        return json.dumps(list_dictionaries)