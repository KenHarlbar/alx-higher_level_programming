#!/usr/bin/python3
""" Base module """
from csv import list_dialects
import json
import os
import csv


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

    @classmethod
    def load_from_file(cls):
        ''' Method that returns a list of instances '''

        filename = f'{cls.__name__}.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_str = f.read()
        list_from_str = cls.from_json_string(list_str)
        list_ins = []
        for i in range(len(list_from_str)):
            list_ins.append(cls.create(**list_from_str[i]))
        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins