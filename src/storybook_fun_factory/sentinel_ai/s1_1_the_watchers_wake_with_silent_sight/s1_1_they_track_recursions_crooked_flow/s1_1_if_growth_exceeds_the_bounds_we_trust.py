# Filename: _1_1_if_growth_exceeds_the_bounds_we_trust.py

import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt


def detect_recursive_overgrowth(graph: nx.DiGraph, growth_threshold: int = 5) -> list[str]:
    """
    Detects nodes in a recursion graph where the number of outgoing edges (NOT only recursive edges) exceeds a threshold.

    Args:
        graph (nx.DiGraph): The recursion graph to scan.
        growth_threshold (int): The maximum allowed out-degree before triggering overgrowth warning.

    Returns:
        list[str]: A list of node names that exceed the growth threshold.
    """
    flagged_nodes = []
    for node in graph.nodes:
        out_degree = graph.out_degree(node)
        if out_degree > growth_threshold:
            flagged_nodes.append(node)
    return flagged_nodes


def mark_overgrowth_on_graph(graph: nx.DiGraph, overgrown_nodes: list[str]) -> None:
    """
    Marks nodes visually within the graph that are flagged for overgrowth.

    Args:
        graph (nx.DiGraph): The graph to update.
        overgrown_nodes (list[str]): List of node labels to mark.
    """
    for node in overgrown_nodes:
        if node in graph:
            graph.nodes[node]["overgrowth"] = True


def render_overgrowth_graph(graph: nx.DiGraph, save_path: Path = None) -> None:
    """
    Renders a visualization of the graph, highlighting overgrown nodes.

    Args:
        graph (nx.DiGraph): The graph to visualize.
        save_path (Path, optional): If provided, saves the image to this path.
    """
    pos = nx.spring_layout(graph, seed=42)
    node_colors = ["#ff6666" if graph.nodes[n].get("overgrowth") else "#9ecae1" for n in graph.nodes()]

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrows=True, arrowstyle="->")
    nx.draw_networkx_labels(graph, pos, font_size=9)
    plt.title("Recursive Overgrowth Detection")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
        ("A", "A"),
        ("A", "C"),
        ("C", "B"),
        ("B", "B"),
        ("B", "A"),
        ("A", "D"),
    ])

    overgrown = detect_recursive_overgrowth(G, growth_threshold=3)
    mark_overgrowth_on_graph(G, overgrown)
    render_overgrowth_graph(G, save_path=Path("sentinel_output/overgrowth_graph.png"))
