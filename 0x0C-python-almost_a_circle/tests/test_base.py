''' Module containing test case for base class'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' A class to test the functionality of base class '''

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        ''' Method to test attribute "id" '''

        self.assertAlmostEqual(Base().id, 1)
        self.assertAlmostEqual(Base().id, 2)
        self.assertAlmostEqual(Base().id, 3)
        self.assertAlmostEqual(Base(12).id, 12)
        self.assertAlmostEqual(Base().id, 4)
        self.assertAlmostEqual(Base('a').id, 'a')