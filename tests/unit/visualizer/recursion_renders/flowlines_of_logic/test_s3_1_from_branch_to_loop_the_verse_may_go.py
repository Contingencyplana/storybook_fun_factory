# Filename: test_s3_1_from_branch_to_loop_the_verse_may_go.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _3_1_from_branch_to_loop_the_verse_may_go as flowline


def test_branch_loop_structure_creates_expected_nodes_and_edges():
    graph = nx.DiGraph()
    root = "Start"
    forks = ["A", "B", "C"]
    reconnect = "Merge"

    updated_graph = flowline.build_branch_loop_diagram(graph, root, forks, reconnect)

    # Root node
    assert root in updated_graph.nodes
    assert updated_graph.nodes[root]["type"] == "branch_origin"

    # Fork nodes and reconnect edges
    for f in forks:
        assert f in updated_graph.nodes
        assert updated_graph.nodes[f]["type"] == "recursive_branch"
        assert updated_graph.has_edge(root, f)
        assert updated_graph.get_edge_data(root, f)["type"] == "fork_edge"
        assert updated_graph.has_edge(f, reconnect)
        assert updated_graph.get_edge_data(f, reconnect)["type"] == "reconnect_edge"

    # Reconnect node
    assert reconnect in updated_graph.nodes
    assert updated_graph.nodes[reconnect]["type"] == "loop_merge"


def test_branch_loop_renders_diagram(tmp_path):
    graph = nx.DiGraph()
    graph = flowline.build_branch_loop_diagram(
        graph,
        root="Ignition",
        forks=["Fork X", "Fork Y"],
        reconnect="Loop Join"
    )

    # Temporary render test
    temp_output = tmp_path / "branch_loop_test.png"
    flowline.render_branch_loop_diagram(graph, save_path=temp_output)
    assert temp_output.exists()
    assert temp_output.stat().st_size > 0

    # Permanent visualizer_output test
    official_output = Path("visualizer_output/from_branch_to_loop_the_verse_may_go.png")
    flowline.render_branch_loop_diagram(graph, save_path=official_output)
    assert official_output.exists()
    assert official_output.stat().st_size > 0
