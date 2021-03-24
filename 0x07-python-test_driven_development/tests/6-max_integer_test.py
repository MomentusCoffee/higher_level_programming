#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([9, 2, 5, 7, 3]), 9)
        self.assertEqual(max_integer([-4, 0, -7, 1]), 0)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([-1.23, -1]), -1)
        self.assertEqual(max_integer([5]), 5)

if __name__ == "__main__":
    unittest.main()
