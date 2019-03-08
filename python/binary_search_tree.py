"""Binary Search Tree.

A Tree is hierarchical data structure with nodes and edges, like a graph, but
unlike a graph, cycles cannot exist in a tree.

A Binary Tree is a tree whose nodes have at most 2 children (left and right).

A Binary Search Tree has the following properties:
 - the left child's value is less than it's parent's node value
 - the right child's value is greater than it's parent's node value
"""
from random import randint


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node {self.value}"

    def __gt__(self, node):
        return self.value > node.value

    def __lt__(self, node):
        return self.value < node.value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            self._add(node, self.root)

    def _add(self, new_node, existing_node):
        if new_node > existing_node:
            if existing_node.right is None:
                existing_node.right = new_node
            else:
                self._add(new_node, existing_node.right)
        elif new_node < existing_node:
            if existing_node.left is None:
                existing_node.left = new_node
            else:
                self._add(new_node, existing_node.left)


bs_tree = BinarySearchTree()

for _ in range(10):
    bs_tree.add(Node(randint(1, 30)))
