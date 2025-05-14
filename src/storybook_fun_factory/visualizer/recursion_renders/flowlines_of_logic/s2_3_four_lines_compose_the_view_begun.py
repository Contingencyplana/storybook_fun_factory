# Filename: s2_3_four_lines_compose_the_view_begun.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def compose_stanza_view(graph: nx.DiGraph, stanza_id: str, line_ids: list[str]) -> nx.DiGraph:
    """
    Renders the emerging stanza structure as a cohesive visual quartet—highlighting symmetry, balance,
    and recursive buildup between the four lines.
    """
    assert len(line_ids) == 4, "A stanza must consist of exactly four lines."

    stanza_node = f"{stanza_id}_view"
    graph.add_node(stanza_node, label=f"Stanza: {stanza_id}", type="stanza_view", style="quartet")

    for line_id in line_ids:
        if line_id not in graph:
            graph.add_node(line_id, label=f"Line: {line_id}", type="unclassified_line")
        graph.add_edge(stanza_node, line_id, type="stanza_composition")

    return graph


def render_stanza_view(graph: nx.DiGraph, save_path: Path = None):
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, "label")

    node_colors = []
    for node in graph.nodes:
        t = graph.nodes[node].get("type", "")
        if t == "stanza_view":
            node_colors.append("#add8e6")  # light blue
        elif t == "unclassified_line":
            node_colors.append("#ffd966")  # soft gold
        else:
            node_colors.append("#cccccc")

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_edges(graph, pos, arrows=True, arrowstyle="->", arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels, font_size=10)
    plt.title("Four Lines Compose the View Begun")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    stanza_id = "stanza_2"
    lines = ["v2_1", "v2_2", "v2_3", "v2_4"]
    G = compose_stanza_view(G, stanza_id, lines)
    render_stanza_view(G, save_path=Path("visualizer_output/four_lines_compose_the_view_begun.png"))

