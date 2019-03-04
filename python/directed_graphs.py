"""Directed Graphs.

Graphs are a non linear data structure consisting of nodes connected by edges.

Graphs can be Directed or Undirected. The edges of a directed graph have an
associated direction, undirected graph edges do not.

Directed graphs can contain cycles (loops from a node, back to itself, possibly
through another node). Directed graphs that have at least one such cycle are
called "cyclic" and those that don't "acyclic" (DAG).
"""
from collections import defaultdict

# Nodes are the keys, and directed edges are the values
directed_acyclic_graph = {
    'A': ['B', 'C'],
    'B': ['G', 'D', 'C'],
    'C': ['D'],
    'D': [],
    'E': ['F'],
    'F': ['C'],
    'G': [],
}

directed_cyclic_graph = {
    'A': ['B', 'C'],
    'B': ['G', 'D', 'C'],
    'C': ['D'],
    'D': ['C'],  # cycle exists between C & D
    'E': ['F'],
    'F': ['C'],
    'G': [],
}


def find_path(graph, start_node, end_node, path=[]):
    """Find any path from start node to end node."""
    path = path + [start_node]  # use assignment (do not append())

    if start_node == end_node:
        # we have found the end node, inform the recursive calls
        return path

    for node in graph[start_node]:
        if node not in path:
            newpath = find_path(graph, node, end_node, path)
            if newpath is not None:
                return newpath

    # you hit a dead end and haven't found the end_node,
    # discard this copy of "path" with the dead end node
    return None


def has_cycles(graph):
    """A directed graph is acyclic if it can be topologically sorted."""
    # count the number of incoming edges each node has
    incoming_edges = defaultdict(int)
    for children in graph.values():
        for child in children:
            incoming_edges[child] += 1

    # start with a node that has no incoming edges
    edgeless_nodes = [node for node in graph if node not in incoming_edges]

    topsorted = []
    while edgeless_nodes:
        node = edgeless_nodes.pop()
        topsorted.append(node)

        # remove the edges for this node
        for dependency in graph[node]:
            incoming_edges[dependency] -= 1
            # check if this node could go next
            if incoming_edges[dependency] == 0:
                edgeless_nodes.append(dependency)
                incoming_edges.pop(dependency)

    # if there are any incoming edges left, the graph has cycles
    if incoming_edges:
        print(f"DAG Topsort order: {topsorted}")
        return True
    return False
