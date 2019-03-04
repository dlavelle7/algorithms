"""Directed Acyclic Graphs (DAG).

[WIP]

Graphs are a network of nodes connected by edges. In directed graphs, these
edges (or arcs) have a direction.

In acyclical graphs, there is no way to start at any node, and loop back around
to that node again. Acyclic graphs have a topological ordering.
"""
from collections import defaultdict



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

def has_cycles(graph):
    """A directed graph is acyclic if it can be topologically sorted."""
    # count the incoming edges of each node
    incoming = defaultdict(int)
    for children in graph.values():
        for child in children:
            incoming[child] += 1

    # start with a node that has no incoming edges
    edgeless_nodes = [node for node in graph if node not in incoming]

    topsorted = []
    while edgeless_nodes:
        node = edgeless_nodes.pop()
        topsorted.append(node)

        # remove the edges for this node
        for dependency in graph[node]:
            incoming[dependency] -= 1
            # check if this node could go next
            if incoming[dependency] == 0:
                edgeless_nodes.append(dependency)

    # if there are any incoming edges left, the graph has cycles
    edges_left = any(incoming_count > 0 for incoming_count in incoming.values())
    if not edges_left:
        print(f"DAG Topsort order: {topsorted}")
    return edges_left
