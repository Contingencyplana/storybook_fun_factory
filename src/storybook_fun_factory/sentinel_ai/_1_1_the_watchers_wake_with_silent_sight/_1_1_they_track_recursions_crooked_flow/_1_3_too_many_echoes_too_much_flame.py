# Filename: _1_3_too_many_echoes_too_much_flame.py

import networkx as nx
from typing import List

def detect_excessive_feedback(graph: nx.DiGraph, feedback_threshold: int = 3) -> List[str]:
    """
    Detects nodes with excessive feedback connections (self-loops or reciprocal edges).

    Args:
        graph (nx.DiGraph): The recursion graph to scan.
        feedback_threshold (int): Maximum allowed feedback edges before flagging.

    Returns:
        List[str]: A list of node names that exceed the feedback threshold.
    """
    flagged_nodes = []
    for node in graph.nodes:
        feedback_edges = 0
        # Count self-loop
        if graph.has_edge(node, node):
            feedback_edges += 1
        # Count mutual edges (back-and-forth)
        for neighbor in graph.successors(node):
            if graph.has_edge(neighbor, node) and neighbor != node:
                feedback_edges += 1
        if feedback_edges > feedback_threshold:
            flagged_nodes.append(node)
    return flagged_nodes


def mark_feedback_nodes(graph: nx.DiGraph, feedback_nodes: List[str], flag_attribute: str = "feedback_hotspot") -> None:
    """
    Flags nodes in the graph identified with excessive feedback.

    Args:
        graph (nx.DiGraph): The graph to update.
        feedback_nodes (List[str]): List of node names to flag.
        flag_attribute (str): The attribute key to mark flagged nodes.
    """
    for node in feedback_nodes:
        if node in graph:
            graph.nodes[node][flag_attribute] = True


if __name__ == "__main__":
    # Example standalone demonstration
    G = nx.DiGraph()
    G.add_edges_from([
        ("A", "B"),
        ("B", "A"),
        ("B", "C"),
        ("C", "B"),
        ("C", "C"),
    ])

    excessive = detect_excessive_feedback(G, feedback_threshold=2)
    mark_feedback_nodes(G, excessive)

    print("Feedback Hotspots:", excessive)
    print("Graph Node Attributes:")
    for node in G.nodes(data=True):
        print(node)
