#!usr/bin/python3
""" Module for class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square which inherits from Rectangle"""

    def __init__(self, size):
        """ Initializes class """

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ method to calculate area of square """

        return self.__size ** 2
