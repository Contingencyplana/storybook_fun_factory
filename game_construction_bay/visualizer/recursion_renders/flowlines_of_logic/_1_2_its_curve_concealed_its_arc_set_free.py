# Filename: _1_2_its_curve_concealed_its_arc_set_free.py
"""
Generates the curve or trajectory of a previously unrendered recursive line.
It maps hidden influence as animated arcs, visualizing how unseen flows were
nonetheless released and shaped the system’s evolution.
"""

import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend for compatibility with test runners

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# Define output directory and file
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "its_curve_concealed_its_arc_set_free.png"

def draw_hidden_curve(output_path=OUTPUT_FILE):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Create a directed graph to illustrate arc divergence and return
    G = nx.DiGraph()

    # Add nodes including hidden and diverging influences
    G.add_node("Start", layer=0)
    G.add_node("Echo A", layer=1)
    G.add_node("???", layer=2)              # Hidden recursive leap
    G.add_node("Decision B", layer=3)
    G.add_node("Arc Influence", layer=3.5)  # Newly visualized side influence
    G.add_node("Path C", layer=4)
    G.add_node("End", layer=5)

    # Add main flow edges and a side arc influence
    G.add_edges_from([
        ("Start", "Echo A"),
        ("Echo A", "???"),
        ("???", "Decision B"),
        ("???", "Arc Influence"),
        ("Arc Influence", "Path C"),
        ("Decision B", "Path C"),
        ("Path C", "End"),
    ])

    # Assign manual positions for vertical layout with arc separation
    pos = {
        "Start": (0, 6),
        "Echo A": (0, 5),
        "???": (0, 4),
        "Decision B": (-1, 3),
        "Arc Influence": (1, 3),
        "Path C": (0, 2),
        "End": (0, 1),
    }

    # Node color: gray for hidden, yellow for influence, blue for rest
    node_colors = []
    for node in G.nodes():
        if node == "???":
            node_colors.append("lightgray")
        elif node == "Arc Influence":
            node_colors.append("khaki")
        else:
            node_colors.append("skyblue")

    # Draw graph
    plt.figure(figsize=(10, 7))
    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_size=2500,
        node_color=node_colors,
        font_size=10,
        font_weight="bold",
        edge_color="gray",
    )

    plt.title("Unseen Flowline: Its Curve Concealed, Its Arc Set Free", fontsize=12)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Trigger generation on import (optional)
draw_hidden_curve()
