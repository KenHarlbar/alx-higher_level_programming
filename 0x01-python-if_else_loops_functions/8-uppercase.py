#!/usr/bin/python3
def uppercase(string):
    output = ''
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            output += "{:c}".format(ord(i) - 32)
        else:
            output += i
    print(output)
