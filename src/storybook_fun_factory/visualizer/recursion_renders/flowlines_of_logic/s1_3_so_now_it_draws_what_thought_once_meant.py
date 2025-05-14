"""
Filename: s1_3_so_now_it_draws_what_thought_once_meant.py

Interprets prior logic in hindsight, rendering the visual narrative of a past recursion.
It draws diagrams that match decisions with their unseen causes, converting abstract
reasoning into visual memory.
"""

import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend for test compatibility

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# Define output directory and file
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "so_now_it_draws_what_thought_once_meant.png"

def draw_logical_reflection(output_path=OUTPUT_FILE):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Create a directed graph to reflect hindsight logic linking
    G = nx.DiGraph()

    # Define nodes: visible, hidden, and retrospective insights
    G.add_node("Start", layer=0)
    G.add_node("Echo A", layer=1)
    G.add_node("???", layer=2)                   # Hidden leap
    G.add_node("Decision B", layer=3)
    G.add_node("Memory Fragment", layer=3.2)     # Retrospective insight
    G.add_node("Path C", layer=4)
    G.add_node("Echo Seen", layer=4.5)           # Retrospective echo
    G.add_node("End", layer=5)

    # Add edges to simulate reflective tracing
    G.add_edges_from([
        ("Start", "Echo A"),
        ("Echo A", "???"),
        ("???", "Decision B"),
        ("Decision B", "Path C"),
        ("Path C", "End"),
        ("???", "Memory Fragment"),         # A past echo unearthed
        ("Memory Fragment", "Echo Seen"),   # Reflective node
        ("Echo Seen", "Decision B"),        # Loops back in awareness
    ])

    # Position nodes for visual clarity
    pos = {
        "Start": (0, 7),
        "Echo A": (0, 6),
        "???": (0, 5),
        "Decision B": (0, 4),
        "Memory Fragment": (-1, 3.5),
        "Path C": (0, 3),
        "Echo Seen": (1, 3.5),
        "End": (0, 2),
    }

    # Assign node colors
    node_colors = []
    for node in G.nodes():
        if node == "???":
            node_colors.append("lightgray")
        elif node in ["Memory Fragment", "Echo Seen"]:
            node_colors.append("khaki")
        else:
            node_colors.append("skyblue")

    # Render the graph
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_size=2500,
        node_color=node_colors,
        font_size=10,
        font_weight="bold",
        edge_color="gray"
    )
    plt.title("Reflective Trace: So Now It Draws What Thought Once Meant", fontsize=12)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Optional auto-run
draw_logical_reflection()
