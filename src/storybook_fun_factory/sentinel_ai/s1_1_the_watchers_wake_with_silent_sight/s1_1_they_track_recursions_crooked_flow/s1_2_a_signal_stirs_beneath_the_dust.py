# Filename: s1_2_a_signal_stirs_beneath_the_dust.py

import networkx as nx
from typing import List


def activate_latent_diagnostics(graph: nx.DiGraph, signal_attribute: str = "latent_signal") -> List[str]:
    """
    Activates latent diagnostic markers in a recursion graph.

    This function scans the graph for nodes that contain a latent signal attribute and surfaces them
    as active points of interest, indicating potential hidden irregularities in the recursion structure.

    Args:
        graph (nx.DiGraph): The recursion graph to scan.
        signal_attribute (str): The attribute key representing latent signals.

    Returns:
        List[str]: A list of node names where latent signals were activated.
    """
    activated_nodes = []
    for node, data in graph.nodes(data=True):
        if signal_attribute in data and data[signal_attribute] is True:
            activated_nodes.append(node)
    return activated_nodes


def flag_activated_nodes(graph: nx.DiGraph, activated_nodes: List[str], flag_attribute: str = "activated") -> None:
    """
    Flags nodes in the graph that have had latent signals activated.

    Args:
        graph (nx.DiGraph): The graph to update.
        activated_nodes (List[str]): List of node names to flag.
        flag_attribute (str): The attribute key to mark as activated.
    """
    for node in activated_nodes:
        if node in graph:
            graph.nodes[node][flag_attribute] = True


if __name__ == "__main__":
    # Example standalone demonstration
    G = nx.DiGraph()
    G.add_nodes_from([
        ("A", {"latent_signal": True}),
        ("B", {}),
        ("C", {"latent_signal": True}),
        ("D", {})
    ])
    G.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "A")
    ])

    activated = activate_latent_diagnostics(G)
    flag_activated_nodes(G, activated)

    print("Activated Nodes:", activated)
    print("Node Attributes After Activation:")
    for node in G.nodes(data=True):
        print(node)
