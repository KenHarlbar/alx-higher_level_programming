#!/usr/bin/python3
"""module containing a square class"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Initialize method for the size of square

        Args:
            size (int): size of square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Method to compute the area of square

        Args:
            self (object): instance of class square
        """

        return self.__size ** 2
