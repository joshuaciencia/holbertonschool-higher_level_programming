#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal_usage(self):
        self.assertEqual(max_integer([3, 9, 18]), 18)

    def test_type(self):
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -36, -3]), -1)

    def test_max_end(self):
        self.assertEqual(max_integer([0, 1, 100]), 100)

    def test_max_beg(self):
        self.assertEqual(max_integer([100, 0, 1]), 100)

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_one_neg(self):
        self.assertEqual(max_integer([1, 2, -1]), 2)

    def test_list_of_one(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
