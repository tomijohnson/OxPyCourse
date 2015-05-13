# Tests the functions and classes contained within ass2
__author__ = 'tomi'

# Imports
import unittest
import ass2


class TestMin(unittest.TestCase):
    def setUp(self):
        self.aeexamples = []
        self.aeexamples.append(([], None))
        self.aeexamples.append(([1], 1))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9], -45))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, "string"], -45))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, []], -45))

    def tearDown(self):
        self.aeexamples = {}

    def test_min(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_min(example[0]), example[1])

    def test_min_iterative(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_min_iterative(example[0]), example[1])

    def test_min_recursive(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_min_recursive(example[0]), example[1])


class TestMax(unittest.TestCase):
    def setUp(self):
        self.aeexamples = []
        self.aeexamples.append(([], None))
        self.aeexamples.append(([1], 1))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9], 34))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, "string"], "string"))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, []], []))

    def tearDown(self):
        self.aeexamples = {}

    def test_max(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_max(example[0]), example[1])

    def test_min_iterative(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_max_iterative(example[0]), example[1])

    def test_min_recursive(self):
        for example in self.aeexamples:
            self.assertEqual(ass2.get_max_recursive(example[0]), example[1])


if __name__ == '__main__':
    unittest.main()
