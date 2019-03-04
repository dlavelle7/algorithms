from unittest import TestCase
from copy import deepcopy

from python.directed_acyclic_graph import find_path, has_cycles

# Nodes are the keys, and directed edges are the values
directed_graph = {
    'A': ['B', 'C'],
    'B': ['G', 'D', 'C'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
    'G': [],
}

directed_acyclic_graph = {
    'A': ['B', 'C'],
    'B': ['G', 'D', 'C'],
    'C': ['D'],
    'D': [],
    'E': ['F'],
    'F': ['C'],
    'G': [],
}
class TestDirectedAcyclicGraph(TestCase):

    def test_find_path_01(self):
        self.assertListEqual(['A', 'B', 'D'],
                             find_path(directed_graph, 'A', 'D'))

    def test_find_path_02(self):
        self.assertListEqual(['E', 'F', 'C', 'D'],
                             find_path(directed_graph, 'E', 'D'))

    def test_find_path_03(self):
        self.assertIsNone(find_path(directed_graph, 'A', 'F'))

    def test_has_cycles_pos_1(self):
        self.assertTrue(has_cycles(directed_graph))

    def test_has_cycles_neg_1(self):
        # remove cycle from D -> C
        self.assertFalse(has_cycles(directed_acyclic_graph))
