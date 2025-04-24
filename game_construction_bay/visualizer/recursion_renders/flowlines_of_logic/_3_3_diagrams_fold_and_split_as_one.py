# Filename: _3_3_diagrams_fold_and_split_as_one.py

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
        graph (nx.DiGraph): The graph to
