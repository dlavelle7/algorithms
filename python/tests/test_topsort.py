import unittest
from python.topsort import topological_sort, create_directed_graph


class TestTopsort(unittest.TestCase):

    def test_topological_sort(self):
        # expected [5, 4, 3, 2, 1] or [3, 5, 4, 2, 1] - see render_graph()
        graph = create_directed_graph()
        topsorted = topological_sort(graph)
        self.assertEqual(topsorted[-1].name, "node 1")
        self.assertEqual(topsorted[-2].name, "node 2")
        self.assertTrue(topsorted[-3].name in ("node 3", "node 4"))
        self.assertTrue(topsorted[-4].name in ("node 4", "node 5"))
        self.assertTrue(topsorted[-5].name in ("node 5", "node 3"))
