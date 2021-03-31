#!/usr/bin/python3
"""
Unitest for Base model


"""
import sys
import os
import inspect
import unittest
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """
    Unittest for class Rectangle
    """
    def test_docstring(self):
        """
        Test if docstring exist
        """
        self.assertIsNotNone(Rectangle.__doc__)
        for i in 

    @classmethod
    def setUpClass(cls):
        """
        Reusable test cases
        """
        Base._Base__nb_objects = 0
        cls.test = Rectangle(2, 2)
        cls.test1 = Rectangle(2, 4, 7)
        cls.test2 = Rectangle(3, 5, 9, 8)
        cls.test3 = Rectangle(5, 8)
        cls.all_functions = 

    def test_id(self):
