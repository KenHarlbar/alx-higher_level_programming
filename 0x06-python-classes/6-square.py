#!/usr/bin/python3
"""module for class square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize method for size of square

        Args:
            size (int): size of square
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Method for retrieving size of square

        Returns:
            size
        """

        return self.__size

    @property
    def position(self):
        """Method for retrieving size of square

        Returns:
            size
        """

        return self.__position

    @size.setter
    def size(self, value):
        """Method for setting size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        

    @size.setter
    def position(self, value):
        """Method for setting size of square"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Method for computing area of square

        Returns:
            area
        """

        return self.__size ** 2

    def my_print(self):
        """Method to display the square"""

        if self.__size == 0:
            print()
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
