# Filename: _2_1_each_path_a_map_from_what_was_said.py

from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt


def ignite_recursive_spark(graph: nx.DiGraph, verse_id: str, metadata: dict = None) -> nx.DiGraph:
    """
    Traces the poetic ignition point of recursion—where each verse triggers a spark,
    and each spark begins a visual thread. This line initiates the stanza’s recursive energy flow.

    Args:
        graph (nx.DiGraph): The visualizer's recursion graph.
        verse_id (str): A unique identifier for the originating verse.
        metadata (dict, optional): Additional data such as source file, timestamp, stanza ID, etc.

    Returns:
        nx.DiGraph: The updated graph with the ignition node added.
    """
    if metadata is None:
        metadata = {}

    node_label = f"Verse: {verse_id}"
    graph.add_node(verse_id, label=node_label, type="verse_origin", **metadata)

    return graph


def render_ignition_graph(graph: nx.DiGraph, save_path: Path = None) -> None:
    """
    Renders and optionally saves the visual thread initiated by a poetic spark.

    Args:
        graph (nx.DiGraph): The graph to visualize.
        save_path (Path, optional): If provided, saves the figure to this path.
    """
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, 'label')

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(graph, pos, node_size=800, node_color="#ffcc99")
    nx.draw_networkx_edges(graph, pos, arrowstyle='->', arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels, font_size=10)
    plt.title("Ignition of Recursive Thread")
    plt.axis('off')

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()
