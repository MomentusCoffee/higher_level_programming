#!/usr/bin/python3
"""
Unitest for Base model


"""
import os
import sys
import inspect
import unittest
import doctest
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    Unittest for class Base
    """
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.allfunctions = inspect.getmembers(Base, inspect.isfunction)
        cls.test = Base()
        cls.test1 = Base()
        cls.test2 = Base(9)
        cls.test3 = Base()

    def test_docstring(self):
        """
        Test if docstring exist
        """
        self.assertIsNotNone(Base.__doc__)
        for i in self.allfunctions:
            self.assertTrue(i[1].__doc__)

    def test_id_itera(self):
        self.assertEqual(self.test.id, 1)
        self.assertEqual(self.test1.id, 2)
        self.assertEqual(self.test2.id, 9)
        self.assertEqual(self.test3.id, 3)
