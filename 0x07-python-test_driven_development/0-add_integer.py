#!/usr/bin/python3
"""Module containing addition function for two \
        parameters"""

def add_integer(a, b=98):
    """Function that adds parameters a and b

    Args:
        a - first number
        b - second number

    Raises:
        TypeError - if a or b are neither integers \
            nor floats

    Returns:
        addition of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
