"""Binary Search Tree.

A Tree is hierarchical data structure with nodes and edges, like a graph, but
unlike a graph, cycles cannot exist in a tree.

A Binary Tree is a tree whose nodes have at most 2 children (left and right).

A Binary Search Tree has the following properties:
 - the left child's value is less than it's parent's node value
 - the right child's value is greater than it's parent's node value
"""
from random import randint
from graphviz import Digraph
from collections import deque


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
        else:
            return  # Don't allow duplicates in this binary search tree

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


def count_tree_nodes(bs_tree):
    """
    Find the number of nodes in a given tree using the Breadth First Search
    algorithm (as opposed to tracking the count in the tree class).
    """
    count = 0
    queue = deque([bs_tree.root]) if bs_tree.root is not None else deque()
    while queue:
        node = queue.popleft()
        count += 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return count


def find_tree_height(bs_tree):
    """
    Find the longest path from the root to a leaf using the Depth First Search
    algorithm (as opposed to tracking the height in the tree class).
    """
    max_height = 0

    def find_branch_height(node, branch_height=None):
        if branch_height is None:
            branch_height = 0
            print("Starting new recursive search")

        branch_height += 1
        print(f"Found new node ({node}), "
              f"incrementing height to {branch_height}")

        nonlocal max_height  # refers to the enclosing function's locals()

        if node.left is None and node.right is None:
            print(f"Reached a leaf node ({node}), "
                  f"branch height: {branch_height}, "
                  f"current max height: {max_height}")
            # reached the end of the line, check if this branch is longest
            if branch_height > max_height:
                max_height = branch_height
                print(f"Set new max height {max_height}")
        else:
            for child in [node.left, node.right]:
                if child is not None:
                    find_branch_height(child, branch_height)

    if bs_tree.root is not None:
        find_branch_height(bs_tree.root)
    return max_height


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
