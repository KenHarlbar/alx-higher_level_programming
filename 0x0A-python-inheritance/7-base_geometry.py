#!/usr/bin/python3
""" BaseGeometry module """


class BaseGeometry:
    """ Class for geometry """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if isinstance(value, int) == False:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
