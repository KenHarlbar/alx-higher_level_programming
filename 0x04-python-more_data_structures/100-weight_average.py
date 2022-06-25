#!/usr/bin/python3
def weight_average(my_list=[]):
    n, d = 0, 0
    if not my_list:
        return 0
    for tup in my_list:
        n += tup[0] * tup[1]
        d += tup[1]
    return n / d
