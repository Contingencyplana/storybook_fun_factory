import pytest
import networkx as nx

from visualizer.recursion_renders.flowlines_of_logic._2_2_each_path_a_map_from_what_was_said import map_logical_flow_from_expression


def test_map_logical_flow_creates_expected_nodes_and_edges():
    graph = nx.DiGraph()

    verse_id = "v1"
    derived_paths = ["v1a", "v1b"]
    metadata = {"source": "test_verse", "line": 2}

    updated_graph = map_logical_flow_from_expression(graph, verse_id, derived_paths, metadata=metadata)

    # Assert the origin node exists
    assert verse_id in updated_graph.nodes
    assert updated_graph.nodes[verse_id]["type"] == "expression_origin"
    assert updated_graph.nodes[verse_id]["source"] == "test_verse"
    assert updated_graph.nodes[verse_id]["line"] == 2

    # Assert the derived nodes and edges exist
    for target in derived_paths:
        assert target in updated_graph.nodes
        assert updated_graph.has_edge(verse_id, target)
        edge_data = updated_graph.get_edge_data(verse_id, target)
        assert edge_data["type"] == "expression_flow"


def test_map_logical_flow_handles_empty_metadata():
    graph = nx.DiGraph()
    verse_id = "vX"
    derived_paths = ["vXa", "vXb"]

    updated_graph = map_logical_flow_from_expression(graph, verse_id, derived_paths)

    assert verse_id in updated_graph.nodes
    assert updated_graph.nodes[verse_id]["type"] == "expression_origin"
    for target in derived_paths:
        assert updated_graph.has_edge(verse_id, target)
