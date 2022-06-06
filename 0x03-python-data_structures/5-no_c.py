#!/usr/bin/python3
def no_c(my_string):
    output = ""
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            continue
        output += letter
    return output
