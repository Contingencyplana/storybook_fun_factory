# Filename: _2_4_where_rhyme_and_rhythm_turn_to_run.py

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path


def animate_recursive_rhythm(graph: nx.DiGraph, layout: str = "spring", interval: int = 1000, save_path: Path = None):
    """
    Finalizes the stanza by animating the motion of recursion.
    Captures poetic rhythm as a living diagram, allowing recursive flow to evolve and loop dynamically.
    """
    if layout == "spring":
        pos = nx.spring_layout(graph, seed=42)
    elif layout == "kamada_kawai":
        pos = nx.kamada_kawai_layout(graph)
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

    ani = animation.FuncAnimation(fig, update, frames=6, interval=interval, repeat=True)

    if save_path:
        ani.save(save_path, writer="pillow")

    plt.show()


if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edge("Spark", "Flow")
    G.add_edge("Flow", "Echo")
    G.add_edge("Echo", "Resolution")
    G.add_edge("Resolution", "Loop")

    output_file = Path("visualizer_output/where_rhyme_and_rhythm_turn_to_run.gif")
    animate_recursive_rhythm(G, layout="spring", save_path=output_file)
