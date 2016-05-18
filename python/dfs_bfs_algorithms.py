from collections import deque
from graphviz import Digraph


class Node(object):
    count = 1

    def __init__(self):
        self.id = Node.count
        self.children = set()
        Node.count += 1

    @property
    def name(self):
        return 'node {0}'.format(self.id)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def add_child(self, child):
        self.children.add(child)


def depth_first_search(root, find_node):

    def recursive_search(node):
        if node.id == find_node:
            return node
        for child in node.children:
            result = recursive_search(child)
            if result:
                return result

    return recursive_search(root)

def breadth_first_search(root, find_node):
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node.id == find_node:
            return node
        for child in node.children:
            queue.append(child)

def create_balanced_tree(levels=3, node=None):
    if not node:
        Node.count = 1
        node = Node()
    if levels > 0:
        node.add_children(set([Node(), Node()]))
        for child in node.children:
            create_balanced_tree(levels - 1, child)
    return node

def render_graph():
    root = create_balanced_tree()
    dot = Digraph('Node_tree')

    def construct_graph(node):
        dot.node(node.name)
        for child in node.children:
            dot.node(child.name)
            dot.edge(node.name, child.name)
            construct_graph(child)

    construct_graph(root)
    dot.render()
