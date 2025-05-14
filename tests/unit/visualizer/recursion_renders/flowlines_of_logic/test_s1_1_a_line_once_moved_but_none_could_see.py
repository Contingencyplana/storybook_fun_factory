# Filename: test_s1_1_a_line_once_moved_but_none_could_see.py

import sys
import os
import pytest
import importlib
from pathlib import Path
import networkx as nx

# 👇 Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

# Constants to check output
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "a_line_once_moved_but_none_could_see.png"

def test_graph_structure():
    G = nx.DiGraph()
    G.add_nodes_from([
        ("Start", {"layer": 0}),
        ("Echo A", {"layer": 1}),
        ("???", {"layer": 2}),
        ("Decision B", {"layer": 3}),
        ("Path C", {"layer": 4}),
        ("End", {"layer": 5}),
    ])
    G.add_edges_from([
        ("Start", "Echo A"),
        ("Echo A", "???"),
        ("???", "Decision B"),
        ("Decision B", "Path C"),
        ("Path C", "End"),
    ])

    assert G.has_node("???")
    assert G.has_edge("Start", "Echo A")
    assert G.has_edge("???", "Decision B")
    assert G.number_of_nodes() == 6
    assert G.number_of_edges() == 5

def test_output_file_creation():
    # Remove existing file before testing
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    # Import and execute the target module
    module = importlib.import_module(
        "visualizer.recursion_renders.flowlines_of_logic._1_1_a_line_once_moved_but_none_could_see"
    )

    # Run the function (assumes the method is named draw_bl_
