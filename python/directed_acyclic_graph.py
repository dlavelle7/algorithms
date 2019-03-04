"""Directed Acyclic Graphs (DAG).

[WIP]

Graphs are a network of nodes connected by edges. In directed graphs, these
edges (or arcs) have a direction.

In acyclical graphs, there is no way to start at any node, and loop back around
to that node again. Acyclic graphs have a topological ordering.
"""


# Nodes are the keys, and directed edges are the values
directed_graph = {
    'A': ['B', 'C'],
    'B': ['G', 'D', 'C'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
    'G': [],
}


def find_path(graph, start_node, end_node, path=[]):
    """Find any path from start node to end node."""
    path = path + [start_node]  # use assignment (not append())

    if start_node == end_node:
        # keep recursing until you hit this point . . .
        return path

    for node in graph[start_node]:
        if node not in path:
            newpath = find_path(graph, node, end_node, path)
            if newpath is not None:
                return newpath

    # . . . or until you hit a dead end and haven't reached end_node,
    # then discard this copy of "path" with the dead end node
    return None


# TODO: Find all paths from one node to another

# TODO: Find the shortest path from one node to another

# TODO: Test if this graph is an acyclic graph or not
