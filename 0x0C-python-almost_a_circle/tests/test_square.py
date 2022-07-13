#!/usr/bin/python3
""" Module for test Square class """

import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base



class TestSquareMethods(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        ''' Method to test id of square '''

        temp = Square(3)
        self.assertEqual(temp.id, 1)
        temp = Square(2, 5, 5, 4)
        self.assertEqual(temp.id, 4)

    def test_width(self):
        ''' Method to test width of square '''

        temp = Square(3)
        self.assertEqual(temp.width, 3)
        temp = Square(2, 5, 5, 4)
        self.assertEqual(temp.width, 2)

    def test_height(self):
        ''' Method to test height of square '''

        temp = Square(3)
        self.assertEqual(temp.height, 3)
        temp = Square(2, 5, 5, 4)
        self.assertEqual(temp.height, 2)

    def test_x(self):
        ''' Method to test x of square '''

        temp = Square(3)
        self.assertEqual(temp.x, 0)
        temp = Square(2, 5, 5, 4)
        self.assertEqual(temp.x, 5)

    def test_y(self):
        ''' Method to test y of square '''

        temp = Square(3)
        self.assertEqual(temp.y, 0)
        temp = Square(2, 5, 5, 4)
        self.assertEqual(temp.y, 5)

    def test_object(self):
        """ Test if instances with the same value are the
        same object """

        temp1 = Square(1, 1)
        temp2 = Square(1, 1)
        self.assertEqual(False, temp1 is temp2)
        self.assertEqual(False, temp1.id == temp2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """

        temp = Square(1)
        self.assertEqual(True, isinstance(temp, Base))

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """

        temp = Square(1)
        self.assertEqual(True, isinstance(temp, Rectangle))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with no args passed """

        with self.assertRaises(TypeError):
            temp = Square()
            temp = Square(-1)
            temp = Square((2+3j))
            temp = Square('a')

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            temp = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs_width(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_height(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_x(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_y(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valid_attrs_size(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_x(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_y(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_x(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_y(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_area_2(self):
        """ Checking the return value of area method """
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())