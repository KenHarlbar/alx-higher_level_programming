#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dico_keys = sorted(a_dictionary.keys())
    for i in dico_keys:
        print(f"{i}: {a_dictionary.get(i)}")
