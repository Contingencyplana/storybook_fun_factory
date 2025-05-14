# Filename: s3_1_from_branch_to_loop_the_verse_may_go.py

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def build_branch_loop_diagram(
    graph: nx.DiGraph,
    root: str,
    forks: list[str],
    reconnect: str,
    metadata: dict = None
) -> nx.DiGraph:
    """
    Builds a diagram showing branching and looping recursion from a root node.
    Each fork leads to intermediate steps and rejoins at a reconnect node, forming a recursive cycle.

    Args:
        graph (nx.DiGraph): An existing graph or new graph to populate.
        root (str): The starting node of the recursive flow.
        forks (list[str]): A list of fork node IDs (intermediate recursive paths).
        reconnect (str): A single node that all branches converge back to.
        metadata (dict, optional): Optional attributes for labeling or styling the root.

    Returns:
        nx.DiGraph: The updated graph.
    """
    if metadata is None:
        metadata = {}

    if root not in graph:
        graph.add_node(root, label=f"Root: {root}", type="branch_origin", **metadata)

    for fork in forks:
        if fork not in graph:
            graph.add_node(fork, label=f"Fork: {fork}", type="recursive_branch")
        graph.add_edge(root, fork, type="fork_edge")

    if reconnect not in graph:
        graph.add_node(reconnect, label=f"Reconnect: {reconnect}", type="loop_merge")
    
    for fork in forks:
        graph.add_edge(fork, reconnect, type="reconnect_edge")

    return graph


def render_branch_loop_diagram(graph: nx.DiGraph, save_path: Path = None):
    """
    Renders the branching loop graph and optionally saves the image to disk.

    Args:
        graph (nx.DiGraph): The graph to visualize.
        save_path (Path, optional): If given, saves the diagram here.
    """
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_node_attributes(graph, 'label')

    color_map = []
    for n in graph.nodes:
        n_type = graph.nodes[n].get("type", "")
        if n_type == "branch_origin":
            color_map.append("#add8e6")  # light blue
        elif n_type == "recursive_branch":
            color_map.append("#ffe599")  # soft yellow
        elif n_type == "loop_merge":
            color_map.append("#b4e197")  # light green
        else:
            color_map.append("#dddddd")

    plt.figure(figsize=(9, 6))
    nx.draw_networkx_nodes(graph, pos, node_color=color_map, node_size=900)
    nx.draw_networkx_edges(graph, pos, arrows=True, arrowstyle="->", arrowsize=15)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10)
    plt.title("From Branch to Loop the Verse May Go")
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    G = nx.DiGraph()
    G = build_branch_loop_diagram(
        G,
        root="Start",
        forks=["Option A", "Option B", "Option C"],
        reconnect="Loop Merge"
    )
    render_branch_loop_diagram(G, save_path=Path("visualizer_output/from_branch_to_loop_the_verse_may_go.png"))
