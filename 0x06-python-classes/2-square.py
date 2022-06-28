#!/usr/bin/python3
"""module containing a square class"""

class Square:
    """Class Square that defines a square
    """

    def __init__(self, size=0):
        """Initialize method for size of square

        Args:
            param1 (int): size of square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = (size)
