# Filename: _1_4_a_flowline_traced_through_firmament.py

import matplotlib.pyplot as plt
import networkx as nx


def draw_complete_flowline(output_path="visualizer_output/a_flowline_traced_through_firmament.png"):
    """
    Links the preceding stanza renderings into one unified poetic-visual arc.
    Traces the movement of recursive logic as it flows, forks, curves, and resolves
    across an entire stanza. Highlights the unseen, the split, the realized, and the recalled.

    This function renders:
    • A 3-tiered poetic graph
    • Key flowlines from prior stanza files
    • Symbolic culmination of recursion visualization
    """

    G = nx.DiGraph()

    # Nodes from previous lines
    G.add_node("Start")
    G.add_node("Blind Arc")
    G.add_node("Fork A")
    G.add_node("Fork B")
    G.add_node("Resolution")
    G.add_node("Echo Return")

    # Additional integration nodes
    G.add_node("???")
    G.add_node("Curve Revealed")
    G.add_node("Final Thread")

    # Edges showing recursive flowline
    G.add_edges_from([
        ("Start", "Blind Arc"),
        ("Blind Arc", "???"),
        ("???", "Fork A"),
        ("???", "Fork B"),
        ("Fork A", "Curve Revealed"),
        ("Fork B", "Resolution"),
        ("Curve Revealed", "Resolution"),
        ("Resolution", "Echo Return"),
        ("Echo Return", "Final Thread")
    ])

    pos = {
        "Start": (0, 3),
        "Blind Arc": (0, 2.5),
        "???": (0, 2),
        "Fork A": (-1, 1.5),
        "Fork B": (1, 1.5),
        "Curve Revealed": (-1, 1),
        "Resolution": (0, 0.5),
        "Echo Return": (0, 0),
        "Final Thread": (0, -0.5),
    }

    colors = {
        "Start": "skyblue",
        "Blind Arc": "lightgray",
        "???": "lightgray",
        "Fork A": "skyblue",
        "Fork B": "skyblue",
        "Curve Revealed": "khaki",
        "Resolution": "lightgreen",
        "Echo Return": "mediumpurple",
        "Final Thread": "gold"
    }

    node_colors = [colors[node] for node in G.nodes()]

    plt.figure(figsize=(10, 7))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color="black",
        node_size=2400,
        font_size=9,
        font_weight="bold",
        arrowsize=20
    )

    plt.title("A Flowline Traced Through Firmament", fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
