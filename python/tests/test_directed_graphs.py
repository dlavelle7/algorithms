from unittest import TestCase
from copy import deepcopy

from python.directed_graphs import (
    find_path, has_cycles, directed_acyclic_graph, directed_cyclic_graph
)


class TestDirectedGraphs(TestCase):

    def test_find_path_01(self):
        self.assertListEqual(['A', 'B', 'D'],
                             find_path(directed_cyclic_graph, 'A', 'D'))

    def test_find_path_02(self):
        self.assertListEqual(['E', 'F', 'C', 'D'],
                             find_path(directed_cyclic_graph, 'E', 'D'))

    def test_find_path_03(self):
        self.assertIsNone(find_path(directed_cyclic_graph, 'A', 'F'))

    def test_has_cycles_pos_1(self):
        self.assertTrue(has_cycles(directed_cyclic_graph))

    def test_has_cycles_neg_1(self):
        self.assertFalse(has_cycles(directed_acyclic_graph))
