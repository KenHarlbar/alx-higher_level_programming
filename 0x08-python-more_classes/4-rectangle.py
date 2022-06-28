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

        Raises:
            TypeError - if width is not an integer
            ValueError - if width is less than 0
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

        Raises:
            TypeError - if width is not an integer
            ValueError - if height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Method that returns the rectangle's area

        Returns:
            area of rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the rectangle's perimeter

        Returns:
            perimeter of rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method to print the rectangle

        Returns:
            string of rectangle
        """

        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for y in range(self.__height):
            rectangle += ("#" * self.__width) + "\n"

        return rectangle.strip()

    def __repr__(self):
        """Method to return the string representation of \
                the rectangle

        Returns:
            string representation of rectangle
        """

        return f'Rectangle({self.__width}, {self.__height})'
