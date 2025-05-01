# Filename: s3_3_diagrams_fold_and_split_as_one.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def build_fold_and_split_diagram(
    graph: nx.DiGraph,
    inputs: list[str],
    fold_point: str,
    outputs: list[str],
    metadata: dict = None
) -> nx.DiGraph:
    """
    Constructs a fold-and-split diagram showing recursive convergence and divergence.

    Args:
        graph (nx.DiGraph): The recursion graph to modify.
        inputs (list[str]): Incoming flow nodes that converge at the fold_point.
        fold_point (str): The central convergence node.
        outputs (list[str]): Outgoing flow nodes that split from the fold_point.
        metadata (dict, optional): Optional metadata for labeling or styling the fold_point.

    Returns:
        nx.DiGraph: The updated graph.
    """
    if metadata is None:
        metadata = {}

    if fold_point not in graph:
        graph.add_node(fold_point, label=f"Fold: {fold_point}", type="confluence", **metadata)

    for i in inputs:
        if i not in graph:
            graph.add_node(i, label=f"Input: {i}", type="input_branch")
        graph.add_edge(i, fold_point, type="converges_into")

    for o in outputs:
        if o not in graph:
            graph.add_node(o, label=f"Output: {o}", type="output_branch")
        graph.add_edge(fold_point, o, type="splits_into")

    return graph


def render_fold_and_split_diagram(graph: nx.DiGraph, save_path: Path = None):
    """
    Renders a visual diagram showing confluence and divergence in recursion.

    Args:
        graph (nx.DiGraph): The graph to draw.
        save_path (Path, optional): If provided, saves the image to this path.
    """
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, 'label')

    node_colors = []
    for node in graph.nodes:
        n_type = graph.nodes[node].get("type", "")
        if n_type == "input_branch":
            node_colors.append("#f9cb9c")  # Light orange
        elif n_type == "confluence":
            node_colors.append("#9fc5e8")  # Light blue
        elif n_type == "output_branch":
            node_colors.append("#b6d7a8")  # Light green
        else:
            node_colors.append("#dddddd")

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=900)
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10)
    plt.title("Diagrams Fold and Split as One")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    build_fold_and_split_diagram(
        G,
        inputs=["Stream A", "Stream B"],
        fold_point="Core Truth",
        outputs=["Branch X", "Branch Y"]
    )
    render_fold_and_split_diagram(G, save_path=Path("visualizer_output/diagrams_fold_and_split_as_one.png"))
