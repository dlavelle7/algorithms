"""Binary Search Tree.

[WIP]

A Tree is hierarchical data structure with nodes and edges, like a graph, but
unlike a graph, cycles cannot exist in a tree.

A Binary Tree is a tree whose nodes have at most 2 children (left and right).

A Binary Search Tree has the following properties:
 - the left child's value is less than it's parent's node value
 - the right child's value is greater than it's parent's node value
"""
from random import randint
from graphviz import Digraph


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return f"Node {self.value}"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            self._add(node, self.root)

    def _add(self, new_node, existing_node):
        if new_node.value > existing_node.value:
            if existing_node.right is None:
                existing_node.right = new_node
            else:
                self._add(new_node, existing_node.right)
        elif new_node.value < existing_node.value:
            if existing_node.left is None:
                existing_node.left = new_node
            else:
                self._add(new_node, existing_node.left)

    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, search_node):
        # TODO: Find path?
        # TODO: Find out how my levels down it was
        if value == search_node.value:
            return search_node
        elif value > search_node.value and search_node.right is not None:
            return self._find(value, search_node.right)
        elif value < search_node.value and search_node.left is not None:
            return self._find(value, search_node.left)


def create_binary_search_tree():
    bs_tree = BinarySearchTree()
    for _ in range(20):
        bs_tree.add(Node(randint(1, 100)))
    return bs_tree


def render_binary_search_tree(bs_tree):
    dot = Digraph("Binary Search Tree")

    def draw_node(node):
        dot.node = node.name
        if node.left is not None:
            dot.edge(node.name, node.left.name)
            draw_node(node.left)
        if node.right is not None:
            dot.edge(node.name, node.right.name)
            draw_node(node.right)

    draw_node(bs_tree.root)

    print(dot.source)
    dot.render()
