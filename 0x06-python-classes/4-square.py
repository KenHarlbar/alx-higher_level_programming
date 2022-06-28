#!/usr/bin/python3
"""module for class square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Initialize method for size of square

        Args:
            size (int): size of square
        """

        self.__size = size

    @property
    def size(self):
        """Method for retrieving size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Method for setting size of square"""

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Method for computing area of square

        Returns:
            area
        """

        return self.__size ** 2
