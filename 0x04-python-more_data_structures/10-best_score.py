#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_of_names = list(a_dictionary.keys())
        max_score = a_dictionary[list_of_names[0]]
        for i in list_of_names:
            if a_dictionary[i]:
                if a_dictionary[i] > max_score:
                    max_score = a_dictionary[i]
                    best_student = i
            else:
                continue
    else:
        return None
    return best_student
