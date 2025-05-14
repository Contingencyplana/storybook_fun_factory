# Filename: s3_4_harmony_drawn_when_paths_are_done.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def close_recursive_harmony(graph: nx.DiGraph, nodes: list[str], loop_edges: list[tuple[str, str]], metadata: dict = None) -> nx.DiGraph:
    """
    Finalizes a stanza's recursion by closing visual logic into harmonic conclusions.
    Each loop represents resolution—where the branching flows complete and echo returns home.

    Args:
        graph (nx.DiGraph): The visualizer graph to complete.
        nodes (list[str]): The core harmonic nodes to highlight.
        loop_edges (list[tuple[str, str]]): Edges forming return cycles or recursive conclusions.
        metadata (dict, optional): Additional styling or identity tags.

    Returns:
        nx.DiGraph: The updated graph.
    """
    if metadata is None:
        metadata = {}

    for node in nodes:
        graph.add_node(node, label=f"Harmony: {node}", type="resolution", **metadata)

    for source, target in loop_edges:
        graph.add_edge(source, target, type="closure")

    return graph


def render_harmonic_resolution(graph: nx.DiGraph, save_path: Path = None):
    """
    Renders a graph showing harmonic resolution—return paths that finalize recursion.

    Args:
        graph (nx.DiGraph): The complete stanza graph.
        save_path (Path, optional): If provided, saves the figure to this path.
    """
    pos = nx.spring_layout(graph, seed=84)
    labels = nx.get_node_attributes(graph, 'label')

    node_colors = []
    for node in graph.nodes:
        n_type = graph.nodes[node].get("type", "")
        if n_type == "resolution":
            node_colors.append("#cfe2f3")  # Soft blue for resolution
        else:
            node_colors.append("#dddddd")  # Default gray

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=14)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10)
    plt.title("Harmony Drawn When Paths Are Done")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    close_recursive_harmony(
        G,
        nodes=["Resolve A", "Resolve B"],
        loop_edges=[("Resolve A", "Resolve B"), ("Resolve B", "Resolve A")]
    )
    render_harmonic_resolution(G, save_path=Path("visualizer_output/harmony_drawn_when_paths_are_done.png"))
