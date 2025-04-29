# Filename: test_2_2_each_path_a_map_from_what_was_said.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _2_2_each_path_a_map_from_what_was_said as flowline


def test_map_logical_flow_creates_origin_and_branches():
    graph = nx.DiGraph()
    origin_id = "v_main"
    derived_paths = ["v_branch_1", "v_branch_2"]
    metadata = {"speaker": "Topsy", "cycle": "Second", "tone": "Reflective"}

    updated_graph = flowline.map_logical_flow_from_expression(graph, origin_id, derived_paths, metadata=metadata)

    assert origin_id in updated_graph.nodes
    origin_data = updated_graph.nodes[origin_id]
    assert origin_data["label"] == "Expr: v_main"
    assert origin_data["type"] == "expression_origin"
    assert origin_data["speaker"] == "Topsy"
    assert origin_data["cycle"] == "Second"
    assert origin_data["tone"] == "Reflective"

    for node in derived_paths:
        assert node in updated_graph.nodes
        assert updated_graph.nodes[node]["type"] == "expression_branch"
        assert updated_graph.has_edge(origin_id, node)
        assert updated_graph.get_edge_data(origin_id, node)["type"] == "expression_flow"


def test_map_logical_flow_handles_empty_metadata_and_reuses_origin():
    graph = nx.DiGraph()
    origin_id = "v_origin"
    derived_paths = ["v1", "v2"]

    graph.add_node(origin_id, label="Expr: v_origin", type="expression_origin")
    updated_graph = flowline.map_logical_flow_from_expression(graph, origin_id, derived_paths)

    assert updated_graph.nodes[origin_id]["label"] == "Expr: v_origin"
    for node in derived_paths:
        assert updated_graph.has_edge(origin_id, node)
        assert updated_graph.nodes[node]["type"] == "expression_branch"


def test_render_expression_graph_creates_image(tmp_path):
    graph = nx.DiGraph()
    graph = flowline.map_logical_flow_from_expression(graph, "origin_2_2", ["branch_x", "branch_y"])

    # Save to tmp path
    temp_output = tmp_path / "expression_flow_test.png"
    flowline.render_expression_graph(graph, save_path=temp_output)

    assert temp_output.exists(), "Image not created"
    assert temp_output.stat().st_size > 0, "Generated image is empty"

    # Save permanent image
    official_path = Path("visualizer_output/each_path_a_map_from_what_was_said.png")
    flowline.render_expression_graph(graph, save_path=official_path)
    assert official_path.exists(), "Permanent visualizer_output image not created"
