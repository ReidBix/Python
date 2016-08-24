__author__ = 'rmb3yz'

import unittest
from graph import Graph


class T1(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph()
        self.g2 = Graph({'A': []})
        self.g3 = Graph({'A': ['B'], 'B': ['A']})
        self.g4 = Graph({'A': ['B'], 'B': ['A', 'C'], 'C': ['B']})
        self.g5 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B']})
        self.g6 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_init_len(self):
        self.assertEqual(len(self.g1), 0, "T1: g1 nodeList length should be 0")
        self.assertEqual(len(self.g2), 1, "T1: g2 nodeList length should be 1")
        self.assertEqual(len(self.g3), 2, "T1: g3 nodeList length should be 2")
        self.assertEqual(len(self.g4), 3, "T1: g4 nodeList length should be 3")
        self.assertEqual(len(self.g5), 4, "T1: g5 nodeList length should be 4")
        self.assertEqual(len(self.g6), 5, "T1: g6 nodeList length should be 5")


class T2(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_get_adjlist(self):
        self.assertEqual(self.g.get_adjlist('A'), ['B', 'D'], "T2: A adjlist should be B, D")
        self.assertEqual(self.g.get_adjlist('B'), ['A', 'D', 'C'], "T2: B adjlist should be A, D, C")
        self.assertEqual(self.g.get_adjlist('C'), ['B'], "T2: C adjlist should be B")
        self.assertEqual(self.g.get_adjlist('D'), ['A', 'B'], "T2: D adjlist should be A, B")
        self.assertEqual(self.g.get_adjlist('E'), [], "T2: E adjlist should be nothing")
        self.assertEqual(self.g.get_adjlist('F'), None, "T2: F adjlist should be None because F doesn't exist")


class T3(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_is_adjacent(self):
        self.assertEqual(self.g.is_adjacent('A', 'B'), True, "T3: A should be adjacent to B")
        self.assertEqual(self.g.is_adjacent('A', 'D'), True, "T3: A should be adjacent to D")
        self.assertEqual(self.g.is_adjacent('B', 'A'), True, "T3: B should be adjacent to A")
        self.assertEqual(self.g.is_adjacent('B', 'D'), True, "T3: B should be adjacent to D")
        self.assertEqual(self.g.is_adjacent('B', 'C'), True, "T3: B should be adjacent to C")
        self.assertEqual(self.g.is_adjacent('C', 'B'), True, "T3: C should be adjacent to B")
        self.assertEqual(self.g.is_adjacent('D', 'A'), True, "T3: D should be adjacent to A")
        self.assertEqual(self.g.is_adjacent('D', 'B'), True, "T3: D should be adjacent to B")
        self.assertEqual(self.g.is_adjacent('A', 'C'), False, "T3: A shouldn't be adjacent to C")
        self.assertEqual(self.g.is_adjacent('A', 'E'), False, "T3: A shouldn't be adjacent to E")
        self.assertEqual(self.g.is_adjacent('B', 'E'), False, "T3: B shouldn't be adjacent to E")
        self.assertEqual(self.g.is_adjacent('C', 'A'), False, "T3: C shouldn't be adjacent to A")
        self.assertEqual(self.g.is_adjacent('C', 'D'), False, "T3: C shouldn't be adjacent to D")
        self.assertEqual(self.g.is_adjacent('C', 'E'), False, "T3: C shouldn't be adjacent to E")
        self.assertEqual(self.g.is_adjacent('D', 'C'), False, "T3: D shouldn't be adjacent to C")
        self.assertEqual(self.g.is_adjacent('D', 'E'), False, "T3: D shouldn't be adjacent to E")
        self.assertEqual(self.g.is_adjacent('E', 'A'), False, "T3: E shouldn't be adjacent to A")
        self.assertEqual(self.g.is_adjacent('E', 'B'), False, "T3: E shouldn't be adjacent to B")
        self.assertEqual(self.g.is_adjacent('E', 'C'), False, "T3: E shouldn't be adjacent to C")
        self.assertEqual(self.g.is_adjacent('E', 'D'), False, "T3: E shouldn't be adjacent to D")
        self.assertEqual(self.g.is_adjacent('Q', 'A'), False, "T3: Q isn't in the graph")
        self.assertEqual(self.g.is_adjacent('A', 'Z'), False, "T3: Z isn't in the graph")


class T4(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_add_node(self):
        self.assertEqual(self.g.add_node('F'), True, "T4: F shouldn't be in g, should return True once added")
        self.assertEqual(len(self.g), 6, "g nodeList length should be 6")
        self.assertEqual(self.g.add_node('G'), True, "T4: G shouldn't be in g, should return True once added")
        self.assertEqual(len(self.g), 7, "g nodeList length should be 7")
        self.assertEqual(self.g.add_node('H'), True, "T4: H shouldn't be in g, should return True once added")
        self.assertEqual(len(self.g), 8, "g nodeList length should be 8")
        self.assertEqual(self.g.add_node('A'), False, "T4: A should already be in g, should return False")
        self.assertEqual(len(self.g), 8, "g nodeList length should remain to be 8")


class T5(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_link_nodes(self):
        self.assertEqual(self.g.link_nodes('A', 'C'), True, "T5: A should be linked to C now")
        self.assertEqual(self.g.link_nodes('B', 'E'), True, "T5: B should be linked to E now")
        self.assertEqual(self.g.link_nodes('E', 'G'), False, "T5: E can't link to G")
        self.assertEqual(self.g.link_nodes('A', 'B'), False, "T5: A can't link to B")
        self.assertEqual(self.g.link_nodes('A', 'A'), False, "T5: A can't link to A")
        self.assertEqual(self.g.link_nodes('G', 'A'), False, "T5: A can't link to A")


class T6(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_unlink_nodes(self):
        self.assertEqual(self.g.unlink_nodes('A', 'B'), True, "T6: A should be unlinked from B now")
        self.assertEqual(self.g.unlink_nodes('B', 'D'), True, "T6: B should be unlinked from D now")
        self.assertEqual(self.g.unlink_nodes('E', 'F'), False, "T6: E can't unlink from F because it doesn't exist")
        self.assertEqual(self.g.unlink_nodes('A', 'A'), False, "T6: A can't unlink from itself")
        self.assertEqual(self.g.unlink_nodes('G', 'A'), False, "T6: G can't unlink from A because it doesn't exist")


class T7(unittest.TestCase):
    def setUp(self):
        self.g = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})

    def test_del_node(self):
        self.assertEqual(self.g.del_node('A'), True, "T7: A should be removed entirely now")
        self.assertEqual(len(self.g), 4, "T7: Length should be 4 now")
        self.assertEqual(self.g.del_node('B'), True, "T7: B should be removed entirely now")
        self.assertEqual(len(self.g), 3, "T7: Length should be 3 now")
        self.assertEqual(self.g.del_node('Q'), False, "T7: Q didn't exist and couldn't be deleted")
        self.assertEqual(len(self.g), 3, "T7: Length should remain to be 3 now")
        self.assertEqual(self.g.del_node('A'), False, "T7: A used to exist and couldn't be deleted")
        self.assertEqual(len(self.g), 3, "T7: Length should remain to be 3 now")


if __name__ == '__main__':
    unittest.main()
