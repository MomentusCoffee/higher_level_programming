#!/usr/bin/python3
"""
Unitest for Base model


"""
import doctest
import unittest
from models.square import Square


class Test_Base(unittest.TestCase):
    """
    Unittest for class Square
    """
    def test_docstring(self):
        """
        Test if docstring exist
        """
        self.assertIsNotNone(Square.__doc__)
