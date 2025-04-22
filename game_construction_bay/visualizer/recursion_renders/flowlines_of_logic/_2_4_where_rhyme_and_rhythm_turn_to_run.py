# Filename: _2_4_where_rhyme_and_rhythm_turn_to_run.py

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_recursive_rhythm(graph: nx.DiGraph, layout: str = "spring", interval: int = 1000):
    """
    Finalizes the stanza by animating the motion of recursion.
    Captures poetic rhythm as a living diagram, allowing recursive flow to evolve and loop dynamically.

    Args:
        graph (nx.DiGraph): A complete stanza graph including verse, flow, and stanza nodes.
        layout (str): Layout algorithm for animation ("spring", "circular", or "kamada_kawai").
        interval (int): Milliseconds between frames in the animation.
    """
    if layout == "spring":
        pos = nx.spring_layout(graph, seed=42)
    elif layout == "kamada_kawai":
        pos = nx.kamada_kawai_layout(graph)  # <-- ✅ removed seed
    elif layout == "circular":
        pos = nx.circular_layout(graph)
    else:
        pos = nx.spring_layout(graph, seed=42)

    fig, ax = plt.subplots(figsize=(8, 6))

    def update(frame):
        ax.clear()
        nx.draw_networkx_nodes(graph, pos, ax=ax, node_size=700, node_color="#d0f0c0")
        nx.draw_networkx_edges(graph, pos, ax=ax, edge_color="#888888", arrows=True)
        nx.draw_networkx_labels(graph, pos, ax=ax, font_size=10)
        ax.set_title("Recursive Rhythm: Flow in Motion")
        ax.axis("off")

    ani = animation.FuncAnimation(fig, update, frames=3, interval=interval, repeat=True)
    plt.show()
