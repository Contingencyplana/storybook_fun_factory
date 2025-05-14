# Filename: test_s1_1_if_growth_exceeds_the_bounds_we_trust.py

import importlib.util
import os
import pytest
import networkx as nx
from pathlib import Path

# Dynamically import the sentinel module from its full path
spec = importlib.util.spec_from_file_location(
    "_1_1_if_growth_exceeds_the_bounds_we_trust",
    os.path.abspath("src/storybook_fun_factory/sentinel_ai/_1_1_the_watchers_wake_with_silent_sight/_1_1_they_track_recursions_crooked_flow/_1_1_if_growth_exceeds_the_bounds_we_trust.py")
)
sentinel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sentinel)


def test_detect_recursive_overgrowth_flags_correct_nodes():
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("X", "X"),  # Self-loop
        ("X", "Y"),
        ("X", "Z"),
        ("X", "W"),
        ("X", "Q"),
        ("Y", "X"),  # Back edge
        ("Z", "X")   # Back edge
    ])

    result = sentinel.detect_recursive_overgrowth(graph, growth_threshold=3)
    assert "X" in result
    assert isinstance(result, list)


def test_mark_overgrowth_on_graph_sets_flag():
    graph = nx.DiGraph()
    graph.add_nodes_from(["A", "B", "C"])
    sentinel.mark_overgrowth_on_graph(graph, ["A", "C"])

    assert graph.nodes["A"].get("overgrowth") is True
    assert graph.nodes["C"].get("overgrowth") is True
    assert graph.nodes["B"].get("overgrowth") is None


def test_render_overgrowth_graph_saves_file(tmp_path):
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("N1", "N2"),
        ("N2", "N3"),
        ("N3", "N1"),
        ("N1", "N1")
    ])
    sentinel.mark_overgrowth_on_graph(graph, ["N1", "N3"])
    output_path = tmp_path / "test_overgrowth_output.png"

    sentinel.render_overgrowth_graph(graph, save_path=output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0
