__author__ = 'horton'

import unittest
from ourqueue import OurQueue

class TestQueue1(unittest.TestCase):

    def setUp(self):
        self.q1 = OurQueue()

    def test_front_empty(self):
        """Q1: test calling front on empty queue"""
        res = self.q1.front()
        self.assertEqual(res, None, "calling front from empty Queue should return None")

class TestQueue2(unittest.TestCase):

    def setUp(self):
        self.q1 = OurQueue()

    def test_remove_empty(self):
        """Q2: test calling remove on empty queue"""
        res = self.q1.remove()
        self.assertEqual(res, None, "removing from empty Queue should return None")
        self.assertEqual(len(self.q1),0, "removing from empty Queue should leave len==0")

class TestQueue3(unittest.TestCase):

    def setUp(self):
        self.q1 = OurQueue([1])

    def test_remove_size1(self):
        """Q3: test calling remove on queue of size 1"""
        res = self.q1.remove()
        self.assertEqual(res,1, "removing from Queue of size 1 should return 1")
        self.assertEqual(len(self.q1), 0, "removing from Queue of size 1 should leave len==0")

if __name__ == '__main__':
    unittest.main()
