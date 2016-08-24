__author__ = 'Reid'

__author__ = 'horton'

import unittest
from hw2_p2 import OurSet

class TestQueue1(unittest.TestCase):

    def setUp(self):
        self.newSet = OurSet([1,2,3,4,5])

    def test_front_empty(self):
        """Q8,Q9: test adding duplicates"""
        self.newSet.add(1)
        self.assertEqual(len(self.newSet), 5)
        self.assertEqual(self.newSet.set, [1,2,3,4,5])
        self.assertEqual(str(self.newSet), "<1, 2, 3, 4, 5>")
        self.newSet.add(2)
        self.assertEqual(len(self.newSet), 5)
        self.assertEqual(self.newSet.set, [1,2,3,4,5])
        self.assertEqual(str(self.newSet), "<1, 2, 3, 4, 5>")


class TestQueue2(unittest.TestCase):

    def setUp(self):
        self.newSet = OurSet([1,2,3,4,5])

    def test_remove_empty(self):
        """Q10: test adding afterwards"""
        self.newSet.add(-1)
        self.assertEqual(len(self.newSet), 6)
        self.assertEqual(self.newSet.set, [1,2,3,4,5,-1])
        self.assertEqual(str(self.newSet), "<1, 2, 3, 4, 5, -1>")

if __name__ == '__main__':
    unittest.main()
