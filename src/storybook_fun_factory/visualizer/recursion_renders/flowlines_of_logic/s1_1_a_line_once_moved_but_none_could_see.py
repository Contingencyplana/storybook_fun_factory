"""
Filename: s1_1_a_line_once_moved_but_none_could_see.py

Captures an invisible transition—a recursive decision or logical leap made within
the assistant or player’s process that was never visualized. It identifies the
"blind spots" in recursive flow and prepares the canvas for rendering unseen arcs.
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# Define output directory
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Create a directed graph representing a hidden recursive leap
G = nx.DiGraph()

# Add nodes representing visible and invisible recursive states
G.add_node("Start", layer=0)
G.add_node("Echo A", layer=1)
G.add_node("???", layer=2)  # The unseen recursive leap
G.add_node("Decision B", layer=3)
G.add_node("Path C", layer=4)
G.add_node("End", layer=5)

# Add edges to simulate narrative flow including the invisible leap
G.add_edges_from([
    ("Start", "Echo A"),
    ("Echo A", "???"),
    ("???", "Decision B"),
    ("Decision B", "Path C"),
    ("Path C", "End"),
])

# Assign positions manually for better vertical layout
pos = {
    "Start": (0, 5),
    "Echo A": (0, 4),
    "???": (0, 3),
    "Decision B": (0, 2),
    "Path C": (0, 1),
    "End": (0, 0),
}

# Define node colors to highlight the invisible transition
node_colors = []
for node in G.nodes():
    if node == "???":
        node_colors.append("lightgray")
    else:
        node_colors.append("skyblue")

# Draw the graph
plt.figure(figsize=(8, 6))
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
plt.title("Recursive Leap: A Line Once Moved But None Could See", fontsize=12)
plt.tight_layout()

# Save to file
output_path = OUTPUT_DIR / "a_line_once_moved_but_none_could_see.png"
plt.savefig(output_path)
plt.close()
