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

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, existing_node):
        if value > existing_node.value:
            if existing_node.right is None:
                existing_node.right = Node(value)
            else:
                self._add(value, existing_node.right)
        elif value < existing_node.value:
            if existing_node.left is None:
                existing_node.left = Node(value)
            else:
                self._add(value, existing_node.left)

    def __contains__(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, search_node):
        if search_node is None:
            return False
        elif value == search_node.value:
            return True
        elif value > search_node.value and search_node.right is not None:
            return self._contains(value, search_node.right)
        elif value < search_node.value and search_node.left is not None:
            return self._contains(value, search_node.left)
        return False

    def height(self):
        # TODO: Determine the height of tree (BFS)
        raise NotImplementedError("Not yet")


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
