#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    list_of_keys = list(a_dictionary.keys())
    for i in list_of_keys:
        new_dict[i] *= 2
    return new_dict
