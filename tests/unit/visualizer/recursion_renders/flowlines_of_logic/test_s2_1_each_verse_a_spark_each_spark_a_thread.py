# Filename: test_s2_1_each_verse_a_spark_each_spark_a_thread.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _2_1_each_verse_a_spark_each_spark_a_thread as flowline


def test_ignite_recursive_spark_adds_node_with_metadata():
    graph = nx.DiGraph()
    verse_id = "verse_001"
    metadata = {"stanza": "2", "line": 1, "source": "test_poem"}

    updated_graph = flowline.ignite_recursive_spark(graph, verse_id, metadata)

    assert verse_id in updated_graph.nodes
    node_data = updated_graph.nodes[verse_id]
    assert node_data["label"] == "Verse: verse_001"
    assert node_data["type"] == "verse_origin"
    assert node_data["stanza"] == "2"
    assert node_data["line"] == 1
    assert node_data["source"] == "test_poem"


def test_ignite_recursive_spark_defaults_to_empty_metadata():
    graph = nx.DiGraph()
    verse_id = "verse_002"

    updated_graph = flowline.ignite_recursive_spark(graph, verse_id)

    assert verse_id in updated_graph.nodes
    node_data = updated_graph.nodes[verse_id]
    assert node_data["label"] == "Verse: verse_002"
    assert node_data["type"] == "verse_origin"


def test_render_ignition_graph_creates_image(tmp_path):
    # Create graph
    graph = nx.DiGraph()
    graph = flowline.ignite_recursive_spark(graph, "test_verse")

    # Save to temporary path
    temp_output = tmp_path / "test_spark_output.png"
    flowline.render_ignition_graph(graph, save_path=temp_output)

    assert temp_output.exists(), "Rendered ignition graph image not created."
    assert temp_output.stat().st_size > 0, "Generated image is empty."

    # Also save official copy to visualizer_output/
    official_path = Path("visualizer_output/each_verse_a_spark_each_spark_a_thread.png")
    flowline.render_ignition_graph(graph, save_path=official_path)
    assert official_path.exists(), "Official visualizer_output image not created."
