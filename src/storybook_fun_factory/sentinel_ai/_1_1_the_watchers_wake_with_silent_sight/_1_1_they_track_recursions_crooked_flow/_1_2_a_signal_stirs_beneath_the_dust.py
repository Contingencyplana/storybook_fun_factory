# Filename: _1_2_a_signal_stirs_beneath_the_dust.py

import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt


def activate_latent_signals(graph: nx.DiGraph, dust_threshold: int = 2) -> list[str]:
    """
    Activates latent diagnostic signals by detecting nodes with low but nonzero recursion activity.
    
    Args:
        graph (nx.DiGraph): The recursion graph to analyze.
        dust_threshold (int): Maximum recursion count to consider a node as "latent anomaly."
    
    Returns:
        list[str]: List of node identifiers that meet the latent signal criteria.
    """
    latent_nodes = []
    for node in graph.nodes:
        out_edges = graph.out_edges(node)
        recursive_edges = [e for e in out_edges if e[1] == node or graph.has_edge(e[1], node)]
        if 0 < len(recursive_edges) <= dust_threshold:
            latent_nodes.append(node)
    return latent_nodes


def mark_latent_signals_on_graph(graph: nx.DiGraph, latent_nodes: list[str]) -> None:
    """
    Marks nodes within the graph that have been identified as latent signal activators.
    
    Args:
        graph (nx.DiGraph): The graph to update.
        latent_nodes (list[str]): List of node labels considered latent anomalies.
    """
    for node in latent_nodes:
        if node in graph:
            graph.nodes[node]["latent_signal"] = True


def render_latent_signal_graph(graph: nx.DiGraph, save_path: Path = None) -> None:
    """
    Renders the graph, highlighting nodes that have latent diagnostic signals activated.

    Args:
        graph (nx.DiGraph): The graph to visualize.
        save_path (Path, optional): If provided, saves the figure to this path.
    """
    pos = nx.spring_layout(graph, seed=24)
    node_colors = ["#ffcc66" if graph.nodes[n].get("latent_signal") else "#9ecae1" for n in graph.nodes()]
    
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrows=True, arrowstyle="->")
    nx.draw_networkx_labels(graph, pos, font_size=9)
    plt.title("Latent Signal Detection")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    # Example standalone demo
    G = nx.DiGraph()
    G.add_edges_from([
        ("A", "A"),
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
        ("D", "D")
    ])

    latent = activate_latent_signals(G, dust_threshold=1)
    mark_latent_signals_on_graph(G, latent)
    render_latent_signal_graph(G, save_path=Path("sentinel_output/latent_signal_graph.png"))
