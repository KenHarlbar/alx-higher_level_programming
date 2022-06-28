#!/usr/bin/python3
"""module containing rectangle class"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize method for width and height \
            of rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method to retrieve width of rectangle

        Returns:
            self.__width
        """

        return self.__width

    @property
    def height(self):
        """Method to retrieve height of rectangle

        Returns:
            self.__height
        """

        return self.__height

    @width.setter
    def width(self, value):
        """Method to set width

        Args:
            width - width of rectangle
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """Method to set height

        Args:
            height - height of rectangle
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
