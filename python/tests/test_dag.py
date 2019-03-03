from unittest import TestCase

from python.directed_acyclic_graph import acyclic_graph, find_paths


class TestDirectedAcyclicGraph(TestCase):

    def test_find_path_01(self):
        self.assertListEqual(['A', 'B', 'D'],
                             find_paths(acyclic_graph, 'A', 'D'))

    def test_find_path_02(self):
        self.assertListEqual(['E', 'F', 'C', 'D'],
                             find_paths(acyclic_graph, 'E', 'D'))
