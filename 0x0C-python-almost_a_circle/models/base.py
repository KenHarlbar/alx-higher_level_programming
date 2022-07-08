#!/usr/bin/python3
""" Base module """


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