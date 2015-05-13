# Tests the functions and classes contained within ass4
__author__ = 'tomi'

# Imports
import unittest
import ass4


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.aeexamples = []
        self.aeexamples.append(([], 1, None))
        self.aeexamples.append(([0], -1, None))
        self.aeexamples.append(([0], 0, 0))
        self.aeexamples.append(([0], 1, None))
        self.aeexamples.append(([0, 1], -1, None))
        self.aeexamples.append(([0, 1], 0, 0))
        self.aeexamples.append(([0, 1], 1, 1))
        self.aeexamples.append(([0, 1], 2, None))
        self.aeexamples.append(([0, 1, 2], -1, None))
        self.aeexamples.append(([0, 1, 2], 0, 0))
        self.aeexamples.append(([0, 1, 2], 1, 1))
        self.aeexamples.append(([0, 1, 2], 2, 2))
        self.aeexamples.append(([0, 1, 2], 3, None))
        self.aeexamples.append(([0, 1, 1], 1, 1))
        self.aeexamples.append(([-45, -1, 0, 3, 8, 9, 9, 12, 21.9, 3], 9, 5))

    def tearDown(self):
        self.aeexamples = {}

    def test_linear(self):
        for example in self.aeexamples:
            self.assertEqual(ass4.linear_search_iterative(example[0], example[1]), example[2])

    def test_binary(self):
        for example in self.aeexamples:
            self.assertEqual(ass4.binary_search(example[0], example[1]), example[2])

    def test_binary_iterative(self):
        for example in self.aeexamples:
            self.assertEqual(ass4.binary_search_iterative(example[0], example[1]), example[2])

    def test_binary_recursive(self):
        for example in self.aeexamples:
            self.assertEqual(ass4.binary_search_recursive(example[0], example[1]), example[2])


if __name__ == '__main__':
    unittest.main()
