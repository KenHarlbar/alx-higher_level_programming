#!/usr/bin/python3
""" Class module for Student """


class Student:
    """ Student class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes Student

        Args:
            first_name: Student first name
            last_name: Student last name
            age: Student age

        Returns:
            nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=''):
        """ Function that retrieves a dictionary representation
        of a Student instance

        Args:
            attr: key(s)

        Returns:
            dictionary representation of a Student Instance
        """
        dico = self.__dict__.copy()

        if type(attr) == list:
            for each in attr:
                if type(each) != str:
                    return dico

            new_dict = {}

            for each in attr:
                try:
                    new_dict[each] = dico[each]
                except Exception:
                    continue
            return new_dict

        return dico
