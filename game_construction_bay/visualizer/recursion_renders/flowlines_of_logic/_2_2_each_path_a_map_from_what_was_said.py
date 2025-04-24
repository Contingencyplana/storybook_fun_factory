# Filename: _2_2_each_path_a_map_from_what_was_said.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def map_logical_flow_from_expression(
    graph: nx.DiGraph,
    origin_id: str,
    derived_ids: list[str],
    metadata: dict = None
) -> nx.DiGraph:
    """
    Constructs the logical flowlines that emerge from spoken or inscribed recursion.
    It maps past expressions into branching visual pathways.
    """
    if metadata is None:
        metadata = {}

    if origin_id not in graph:
        graph.add_node(origin_id, label=f"Expr: {origin_id}", type="expression_origin", **metadata)

    for target_id in derived_ids:
        if target_id not in graph:
            graph.add_node(target_id, label=f"Path: {target_id}", type="expression_branch")
        graph.add_edge(origin_id, target_id, type="expression_flow")

    return graph


def render_expression_graph(graph: nx.DiGraph, save_path: Path = None):
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, 'label')

    node_colors = []
    for n in graph.nodes:
        t = graph.nodes[n].get("type", "")
        if t == "expression_origin":
            node_colors.append("#add8e6")  # Light blue
        elif t == "expression_branch":
            node_colors.append("#ffe599")  # Pale yellow
        else:
            node_colors.append("#cccccc")

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrowstyle='->', arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels, font_size=10)
    plt.title("Expression to Flow Mapping")
    plt.axis('off')

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    G = map_logical_flow_from_expression(G, "verse_2_2", ["path_a", "path_b"], metadata={"cycle": "Second"})
    render_expression_graph(G, save_path=Path("visualizer_output/each_path_a_map_from_what_was_said.png"))
