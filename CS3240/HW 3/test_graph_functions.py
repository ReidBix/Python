__author__ = 'rmb3yz'

import unittest
from graph import Graph
from graph_functions import is_complete
from graph_functions import nodes_by_degree


class T1(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph()
        self.g2 = Graph({'A': []})
        self.g3 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
        self.g4 = Graph(
            {'A': ['B', 'C', 'D', 'E'], 'B': ['A', 'D', 'C', 'E'], 'C': ['B', 'A', 'D', 'E'], 'D': ['A', 'B', 'C', 'E'],
             'E': ['A', 'B', 'C', 'D']})
        self.g5 = []

    def test_is_complete(self):
        self.assertEqual(is_complete(self.g1), True, "T1: g1 is complete by definition of graph of 0, True")
        self.assertEqual(is_complete(self.g2), True, "T1: g2 is complete by definition of graph of 1, True")
        self.assertEqual(is_complete(self.g3), False, "T1: g3 is obviously not complete")
        self.assertEqual(is_complete(self.g4), True, "T1: g4 is by definition complete, True")
        self.assertEqual(is_complete(self.g5), None, "T1: g5 is not a graph")


class T2(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph()
        self.g2 = Graph({'A': []})
        self.g3 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
        self.g4 = Graph(
            {'A': ['B', 'C', 'D', 'E'], 'B': ['A', 'D', 'C', 'E'], 'C': ['B', 'A', 'D', 'E'], 'D': ['A', 'B', 'C', 'E'],
             'E': ['A', 'B', 'C', 'D']})
        self.g5 = []

    def test_nodes_by_degree(self):
        self.assertEqual(nodes_by_degree(self.g1), [], "T2: g1 should be blank")
        self.assertEqual(nodes_by_degree(self.g2), [('A', 0)], "T2: g2 should contain 1 element")
        self.assertEqual(nodes_by_degree(self.g3), [('B', 3), ('A', 2), ('D', 2), ('C', 1), ('E', 0)],
                         "T2: g3 should contain 5 elements with each neighbors from 3 to 0")
        self.assertEqual(nodes_by_degree(self.g4), [('A', 4), ('B', 4), ('C', 4), ('D', 4), ('E', 4)],
                         "T2: g4 should be 5 elements with each neighbors of 4, a complete graphl")
        self.assertEqual(nodes_by_degree(self.g5), None, "T2: g5 is not a graph")


if __name__ == '__main__':
    unittest.main()
