#!/usr/bin/python3
def weight_average(my_list=[]):
    n, d, product = 0, 0, 1
    if not my_list:
        return 0
    for each in my_list:
        l = len(each)
        for i in range(0, l):
            product *= each[i]
        n += product
        product = 1
        print(n)
        d += each[l - 1]
        print(d)
    return n / d
