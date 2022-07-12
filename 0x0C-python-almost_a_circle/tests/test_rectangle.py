''' Test module for rectangle class '''

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    ''' class to test rectangle '''

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inherit(self):
        ''' Method to test the inheritance of Rectangle
        from Base '''

        self.assertEqual(Rectangle().id, 1)
        self.assertEqual(Rectangle(10, 2).id, 2)
        self.assertEqual(Rectangle(2, 10).id, 3)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)