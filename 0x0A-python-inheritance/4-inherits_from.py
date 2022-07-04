#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """method for comparing type of an instance to a class

    Args:
        obj: instance / object
        a_class: class

    Return:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        False: if otherwise
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
