from unittest import TestCase

from python.binary_search_tree import BinarySearchTree, Node


class TestBinarySearchTree(TestCase):

    def test_binary_search_tree(self):
        bs_tree = BinarySearchTree()
        root = Node(10)
        bs_tree.add(root)
        self.assertIs(bs_tree.root, root)

        node_6 = Node(6)
        bs_tree.add(node_6)
        self.assertIs(root.left, node_6)

        node_14 = Node(14)
        bs_tree.add(node_14)
        self.assertIs(root.right, node_14)

        node_22 = Node(22)
        bs_tree.add(node_22)
        self.assertIs(node_14.right, node_22)
