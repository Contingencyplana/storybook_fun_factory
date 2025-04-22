# Filename: test_2_2_each_path_a_map_from_what_was_said.py

import pytest
import networkx as nx

from visualizer.recursion_renders.flowlines_of_logic._2_2_each_path_a_map_from_what_was_said import map_logical_flow_from_expression


def test_map_logical_flow_creates_origin_and_branches():
    graph = nx.DiGraph()
    origin_id = "v_main"
    derived_paths = ["v_branch_1", "v_branch_2"]
    metadata = {"speaker": "Topsy", "cycle": "Second", "tone": "Reflective"}

    updated_graph = map_logical_flow_from_expression(graph, origin_id, derived_paths, metadata=metadata)

    # Check origin node
    assert origin_id in updated_graph.nodes
    origin_data = updated_graph.nodes[origin_id]
    assert origin_data["label"] == "Expr: v_main"
    assert origin_data["type"] == "expression_origin"
    assert origin_data["speaker"] == "Topsy"
    assert origin_data["cycle"] == "Second"
    assert origin_data["tone"] == "Reflective"

    # Check derived nodes and edges
    for node in derived_paths:
        assert node in updated_graph.nodes
        assert updated_graph.nodes[node]["type"] == "expression_branch"
        assert updated_graph.has_edge(origin_id, node)
        assert updated_graph.get_edge_data(origin_id, node)["type"] == "expression_flow"


def test_map_logical_flow_handles_empty_metadata_and_reuses_origin():
    graph = nx.DiGraph()
    origin_id = "v_origin"
    derived_paths = ["v1", "v2"]

    # Pre-add origin node
    graph.add_node(origin_id, label="Expr: v_origin", type="expression_origin")

    updated_graph = map_logical_flow_from_expression(graph, origin_id, derived_paths)

    # Should not overwrite existing origin node
    assert updated_graph.nodes[origin_id]["label"] == "Expr: v_origin"

    for node in derived_paths:
        assert updated_graph.has_edge(origin_id, node)
        assert updated_graph.nodes[node]["type"] == "expression_branch"
