# Filename: test_2_3_four_lines_compose_the_view_begun.py

import pytest
import networkx as nx

from visualizer.recursion_renders.flowlines_of_logic._2_3_four_lines_compose_the_view_begun import compose_stanza_view


def test_compose_stanza_view_creates_stanza_node_and_links_lines():
    graph = nx.DiGraph()
    stanza_id = "stanza_2"
    line_ids = ["v1", "v2", "v3", "v4"]

    updated_graph = compose_stanza_view(graph, stanza_id, line_ids)

    stanza_node = f"{stanza_id}_view"
    assert stanza_node in updated_graph.nodes
    stanza_data = updated_graph.nodes[stanza_node]

    assert stanza_data["label"] == "Stanza: stanza_2"
    assert stanza_data["type"] == "stanza_view"
    assert stanza_data["style"] == "quartet"

    for line in line_ids:
        assert line in updated_graph.nodes
        assert updated_graph.has_edge(stanza_node, line)
        edge_data = updated_graph.get_edge_data(stanza_node, line)
        assert edge_data["type"] == "stanza_composition"


def test_compose_stanza_view_requires_four_lines():
    graph = nx.DiGraph()
    stanza_id = "stanza_x"
    with pytest.raises(AssertionError, match="A stanza must consist of exactly four lines."):
        compose_stanza_view(graph, stanza_id, ["only_one_line"])
