#!/usr/bin/python3
""" class Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """ class rectangle defining rectangles """

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """ Initializes rectangle
        
        Args: 
            width: width of rectangle
            height: height of rectangle
            x: position of rectangle with respect to the x axis
            y: position of rectangle with respect to the y axis
            id: identification of rectangle
        
        Return:
            Nothing
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    @property
    def width(self, value):
        """ Width getter """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Width setter 
        
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError('Width must be integer')
        if value <= 0:
            raise ValueError('Width must be > 0')
        self.__width = value
    
    @property
    def height(self, value):
        """ Height getter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Height setter 
        
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than or equal to 0
        """

        if type(value) != int:
            raise TypeError('Height must be an integer')
        if value <= 0:
            raise ValueError('Height must be > 0')
        self.__height = value
    
    @property
    def x(self, value):
        """ Position on x-axis getter """
        return self.__x
    
    @x.setter  
    def x(self, value):
        """ x setter 
        
        Raises:
            TypeError: if x is not int
            ValueError: if x is less than 0
        """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
    
    @property
    def y(self, value):
        """ Position on y-axis getter """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ y setter
        
        Raises:
            TypeError: if y is not int
            ValueError: if y is less than 0
        """

        if type(value) is not int:
            raise TypeError('y must be an int')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Method to compute area of rectangle
        
        Returns:
            area
        """
        return self.__width * self.__height

    def display(self):
        """ Method to display rectangle """

        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print('\n', end='')