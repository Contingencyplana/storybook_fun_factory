# Filename: test_3_4_harmony_drawn_when_paths_are_done.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _3_4_harmony_drawn_when_paths_are_done as flowline


def test_close_recursive_harmony_adds_nodes_and_loops():
    graph = nx.DiGraph()
    nodes = ["Node1", "Node2"]
    loop_edges = [("Node1", "Node2"), ("Node2", "Node1")]
    graph = flowline.close_recursive_harmony(graph, nodes, loop_edges)

    for node in nodes:
        assert node in graph.nodes
        assert graph.nodes[node]["type"] == "resolution"
        assert graph.nodes[node]["label"] == f"Harmony: {node}"

    for src, tgt in loop_edges:
        assert graph.has_edge(src, tgt)
        assert graph.get_edge_data(src, tgt)["type"] == "closure"


def test_render_harmonic_resolution_saves_image(tmp_path):
    graph = nx.DiGraph()
    nodes = ["LoopA", "LoopB"]
    loop_edges = [("LoopA", "LoopB"), ("LoopB", "LoopA")]
    graph = flowline.close_recursive_harmony(graph, nodes, loop_edges)

    # Save to temporary file
    temp_output = tmp_path / "harmonic_render_test.png"
    flowline.render_harmonic_resolution(graph, save_path=temp_output)

    assert temp_output.exists()
    assert temp_output.stat().st_size > 0

    # Also verify official render location
    official_output = Path("visualizer_output/harmony_drawn_when_paths_are_done.png")
    flowline.render_harmonic_resolution(graph, save_path=official_output)

    assert official_output.exists()
    assert official_output.stat().st_size > 0
