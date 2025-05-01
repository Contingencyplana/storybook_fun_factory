# Filename: test_s2_3_four_lines_compose_the_view_begun.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _2_3_four_lines_compose_the_view_begun as flowline


def test_compose_stanza_view_creates_stanza_node_and_links_lines():
    graph = nx.DiGraph()
    stanza_id = "stanza_2"
    line_ids = ["v1", "v2", "v3", "v4"]

    updated_graph = flowline.compose_stanza_view(graph, stanza_id, line_ids)

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
        flowline.compose_stanza_view(graph, stanza_id, ["only_one_line"])


def test_render_stanza_view_creates_image(tmp_path):
    graph = nx.DiGraph()
    stanza_id = "test_stanza"
    lines = ["a", "b", "c", "d"]
    graph = flowline.compose_stanza_view(graph, stanza_id, lines)

    tmp_output = tmp_path / "view_test.png"
    flowline.render_stanza_view(graph, save_path=tmp_output)

    assert tmp_output.exists(), "Temp image not created"
    assert tmp_output.stat().st_size > 0, "Generated image is empty"

    official_path = Path("visualizer_output/four_lines_compose_the_view_begun.png")
    flowline.render_stanza_view(graph, save_path=official_path)
    assert official_path.exists(), "Permanent visualizer_output image not created"
