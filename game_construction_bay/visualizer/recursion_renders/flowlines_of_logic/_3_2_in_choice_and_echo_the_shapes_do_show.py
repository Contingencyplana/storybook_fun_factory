# Filename: _3_2_in_choice_and_echo_the_shapes_do_show.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def build_choice_echo_graph(
    graph: nx.DiGraph,
    root: str,
    choices: list[tuple[str, str]],
    metadata: dict = None
) -> nx.DiGraph:
    """
    Creates a mirrored graph of decisions and their echoes.

    Args:
        graph (nx.DiGraph): The visual recursion graph.
        root (str): The node representing the original decision point.
        choices (list[tuple[str, str]]): Each tuple contains (choice_id, echo_id).
        metadata (dict, optional): Optional metadata for the root node.

    Returns:
        nx.DiGraph: The updated graph with decision and echo nodes.
    """
    if metadata is None:
        metadata = {}

    if root not in graph:
        graph.add_node(root, label=f"Decision: {root}", type="decision_root", **metadata)

    for choice_id, echo_id in choices:
        if choice_id not in graph:
            graph.add_node(choice_id, label=f"Choice: {choice_id}", type="choice")
        if echo_id not in graph:
            graph.add_node(echo_id, label=f"Echo: {echo_id}", type="echo")

        graph.add_edge(root, choice_id, type="choice_path")
        graph.add_edge(choice_id, echo_id, type="echo_reflection")

    return graph


def render_choice_echo_graph(graph: nx.DiGraph, save_path: Path = None):
    """
    Renders the mirrored graph of choices and echoes.

    Args:
        graph (nx.DiGraph): The graph to draw.
        save_path (Path, optional): If given, saves the diagram here.
    """
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, 'label')

    node_colors = []
    for n in graph.nodes:
        t = graph.nodes[n].get("type", "")
        if t == "decision_root":
            node_colors.append("#add8e6")  # Light blue
        elif t == "choice":
            node_colors.append("#ffe599")  # Yellow
        elif t == "echo":
            node_colors.append("#d9ead3")  # Light green
        else:
            node_colors.append("#dddddd")  # Default

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=900)
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10)
    plt.title("In Choice and Echo the Shapes Do Show")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    choices = [
        ("Left Path", "Left Reflection"),
        ("Right Path", "Right Reflection"),
        ("Middle Path", "Middle Reflection")
    ]
    build_choice_echo_graph(G, root="Decision Point", choices=choices)
    render_choice_echo_graph(G, save_path=Path("visualizer_output/in_choice_and_echo_the_shapes_do_show.png"))
