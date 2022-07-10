#!/usr/bin/python3
""" Base module """
from csv import list_dialects
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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Method that writes the JSON string representation
        of list_objs to a file'''

        filename = f'{cls.__name__}.json'
        list_dict = []
        if not list_objs:
            pass
        else:
            for i in list_objs:
                list_dict.append(i.to_dictionary())
        lists = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(lists)
    
    @staticmethod
    def from_json_string(json_string):
        ''' Method that returns the list representation of a
        json string'''

        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        ''' Method that create an instance of a class and
        updates it'''

        if cls.__name__ == 'Rectangle':
            dummy = cls(9, 17)
        else:
            dummy = cls(15)
        dummy.update(**dictionary)
        return dummy