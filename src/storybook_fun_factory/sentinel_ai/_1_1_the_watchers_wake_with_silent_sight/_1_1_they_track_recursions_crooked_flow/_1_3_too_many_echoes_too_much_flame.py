# Filename: _1_3_too_many_echoes_too_much_flame.py

import networkx as nx
from typing import List

def detect_recursive_feedback_loops(graph: nx.DiGraph, echo_threshold: int = 2) -> List[str]:
    """
    Detects nodes in a recursion graph where feedback amplification occurs excessively.

    Args:
        graph (nx.DiGraph): The recursion graph to analyze.
        echo_threshold (int): The number of cyclic connections tolerated before flagging instability.

    Returns:
        List[str]: List of node names showing signs of excessive recursive feedback.
    """
    feedback_nodes = []
    for node in graph.nodes:
        cycles_through_node = list(nx.simple_cycles(graph))
        count = sum(1 for cycle in cycles_through_node if node in cycle)
        if count > echo_threshold:
            feedback_nodes.append(node)
    return feedback_nodes

def mark_feedback_nodes(graph: nx.DiGraph, feedback_nodes: List[str], attribute: str = "unstable") -> None:
    """
    Marks nodes that exhibit excessive feedback amplification.

    Args:
        graph (nx.DiGraph): The graph to annotate.
        feedback_nodes (List[str]): List of node names showing instability.
        attribute (str): Attribute key used to flag unstable nodes.
    """
    for node in feedback_nodes:
        if node in graph:
            graph.nodes[node][attribute] = True

if __name__ == "__main__":
    # Example standalone demonstration
    G = nx.DiGraph()
    G.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),  # Cycle A -> B -> C -> A
        ("C", "D"),
        ("D", "C"),  # Cycle C <-> D
        ("B", "D")
    ])

    feedback = detect_recursive_feedback_loops(G, echo_threshold=1)
    mark_feedback_nodes(G, feedback)

    print("Feedback Amplified Nodes:", feedback)
    print("Node Attributes After Flagging:")
    for node in G.nodes(data=True):
        print(node)
