# Filename: test_2_1_each_verse_a_spark_each_spark_a_thread.py

import pytest
import networkx as nx
from visualizer.recursion_renders.flowlines_of_logic._2_1_each_verse_a_spark_each_spark_a_thread import ignite_recursive_spark


def test_ignite_recursive_spark_adds_node_with_metadata():
    graph = nx.DiGraph()
    verse_id = "verse_001"
    metadata = {"stanza": "2", "line": 1, "source": "test_poem"}

    updated_graph = ignite_recursive_spark(graph, verse_id, metadata)

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

    updated_graph = ignite_recursive_spark(graph, verse_id)

    assert verse_id in updated_graph.nodes
    node_data = updated_graph.nodes[verse_id]
    assert node_data["label"] == "Verse: verse_002"
    assert node_data["type"] == "verse_origin"
