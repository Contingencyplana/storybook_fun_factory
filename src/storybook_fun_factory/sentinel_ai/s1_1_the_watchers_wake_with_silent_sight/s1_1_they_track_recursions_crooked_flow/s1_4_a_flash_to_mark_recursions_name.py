# Filename: s1_4_a_flash_to_mark_recursions_name.py

import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt
from typing import List


def finalize_sentinel_flare(graph: nx.DiGraph, critical_nodes: List[str], flare_attribute: str = "sentinel_flare") -> None:
    """
    Finalizes the sentinel flare by marking critical nodes where recursion exceeded safe parameters.

    Args:
        graph (nx.DiGraph): The graph to update.
        critical_nodes (List[str]): List of node names that triggered the sentinel alert.
        flare_attribute (str): The attribute key used to mark the flare event.
    """
    for node in critical_nodes:
        if node in graph:
            graph.nodes[node][flare_attribute] = True


def visualize_sentinel_flare(graph: nx.DiGraph, save_path: Path = None) -> None:
    """
    Visualizes the recursion graph, highlighting nodes where sentinel flares were activated.

    Args:
        graph (nx.DiGraph): The graph to visualize.
        save_path (Path, optional): If provided, saves the visualization to this path.
    """
    pos = nx.spring_layout(graph, seed=42)
    node_colors = ["#ff4d4d" if graph.nodes[n].get("sentinel_flare") else "#9ecae1" for n in graph.nodes()]

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrows=True, arrowstyle="->")
    nx.draw_networkx_labels(graph, pos, font_size=9)
    plt.title("Sentinel Flare Activation")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    # Example standalone demonstration
    G = nx.DiGraph()
    G.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
        ("D", "E"),
        ("E", "D")
    ])
    critical = ["A", "E"]
    finalize_sentinel_flare(G, critical)
    visualize_sentinel_flare(G, save_path=Path("sentinel_output/sentinel_flare_demo.png"))
