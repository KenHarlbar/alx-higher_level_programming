#!/usr/bin/python3
''' Module for Square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Class Square defining squares '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Initializes Square

        Args:
            size: size of square
            x: Square's position on the x-axis
            y: Square's position on the y-axis
            id: Square's id
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Method for printing square '''

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        ''' size getter '''

        return self.width

    @size.setter
    def size(self, value):
        ''' Size setter '''

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' Method to update attributes '''

        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' Method that returns the dictionary representation
        of class '''

        list_attr = ['id', 'size', 'x', 'y']
        dico = {}
        for key in list_attr:
            dico[key] = getattr(self, key)
        return dico
