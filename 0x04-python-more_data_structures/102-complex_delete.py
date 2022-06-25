#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return
    list_of_keys = list(a_dictionary.keys())
    for each in list_of_keys:
        if a_dictionary[each] == value:
            del a_dictionary[each]
    return a_dictionary
