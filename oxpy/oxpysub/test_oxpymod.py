# Tests the functions and classes contained within oxpymod
__author__ = 'tomi'

# Imports
import unittest
import oxpymod


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Setup code
        self.example = 0

    def tearDown(self):
        # Clean up code
        self.example = 0

    def test_something(self):
        # self.assertEqual(a, b)
        # self.assertTrue(a)
        # self.assertTrue(a)
        # self.assertRaises(a)
        self.assertEqual(1,1)

    def test_somethingelse(self):
        # self.assertEqual(a, b)
        # self.assertTrue(a)
        # self.assertTrue(a)
        # self.assertRaises(a)
        self.assertEqual(1,1)

class MyTestCase2(unittest.TestCase):
    def setUp(self):
        # Setup code
        self.example = 0

    def tearDown(self):
        # Clean up code
        self.example = 0

    def test_something(self):
        # self.assertEqual(a, b)
        # self.assertTrue(a)
        # self.assertTrue(a)
        # self.assertRaises(a)
        self.assertEqual(1,1)

    def test_somethingelse(self):
        # self.assertEqual(a, b)
        # self.assertTrue(a)
        # self.assertTrue(a)
        # self.assertRaises(a)
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
