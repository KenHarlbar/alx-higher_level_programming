#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ Function that checks if an object is an instance of,
    or if the object is an instance of a class that inherited from

    Args:
        obj: instance
        a_class: class

    Return:
        True: if obj is an instance of a_class or if obj is an instance
        of a class that inherited from a_class
        False: if otherwise
    """
    return isinstance(obj, a_class)
