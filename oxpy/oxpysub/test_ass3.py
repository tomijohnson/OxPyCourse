# Tests the functions and classes contained within ass3
__author__ = 'tomi'

# Imports
import unittest
import ass3


class TestSort(unittest.TestCase):
    def setUp(self):
        self.aeexamples = []
        self.aeexamples.append(([], []))
        self.aeexamples.append(([1], [1]))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9], [-45, -1, 0, 3, 8, 9, 9, 12, 21.9, 34]))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, "string"], [-45, -1, 0, 3, 8, 9, 9, 12, 21.9, 34, "string"]))
        self.aeexamples.append(([0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9, []], [-45, -1, 0, 3, 8, 9, 9, 12, 21.9, 34, []]))

    def tearDown(self):
        self.aeexamples = {}

    def test_sort(self):
        for example in self.aeexamples:
            self.assertEqual(ass3.sort_list(example[0]), example[1])

    def test_sort_modifier(self):
        for example in self.aeexamples:
            self.assertEqual(ass3.sort_list_modifier(example[0]), example[1])

    def test_sort_pure(self):
        for example in self.aeexamples:
            self.assertEqual(ass3.sort_list_pure(example[0]), example[1])

    def test_sort_bubble(self):
        for example in self.aeexamples:
            self.assertEqual(ass3.bubble_sort(example[0]), example[1])


if __name__ == '__main__':
    unittest.main()
