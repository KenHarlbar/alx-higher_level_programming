#!/usr/bin/python
""" Module containing pascal triangle function """


def pascal_triangle(n):
    """ Function that returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n: length of triangle

    Return:
        List of lists
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        new_list = []
        for j in range(len(result[-1]) + 1):
            new_list.append(temp[j] + temp[j + 1])
        result.append(new_list)
    return result
