#!/usr/bin/python3
class Square:
    """Class Square that defines a square with \
            a private attribute 'size'
    """
    def __init__(self, size):
        """Initialize method that stores the size \
                of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size
