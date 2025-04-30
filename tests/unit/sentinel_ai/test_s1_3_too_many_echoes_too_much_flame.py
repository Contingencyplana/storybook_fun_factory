# Filename: test_1_3_too_many_echoes_too_much_flame.py

import sys
import os
import importlib.util
from pathlib import Path
import pytest
import networkx as nx

# Dynamically load the target file
target_path = Path("src/storybook_fun_factory/sentinel_ai/_1_1_the_watchers_wake_with_silent_sight/_1_1_they_track_recursions_crooked_flow/_1_3_too_many_echoes_too_much_flame.py").resolve()
spec = importlib.util.spec_from_file_location("_1_3_too_many_echoes_too_much_flame", target_path)
sentinel_echo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sentinel_echo)

def test_detect_excessive_feedback_flags_nodes():
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("A", "A"),  # Self-loop (1)
        ("A", "B"),
        ("B", "A"),  # Back edge (2)
        ("A", "C"),
        ("C", "A"),  # Another back edge (3)
        ("A", "D"),
        ("D", "A")   # Yet another back edge (4) -> should trigger detection
    ])

    result = sentinel_echo.detect_excessive_feedback(graph, feedback_threshold=3)
    assert isinstance(result, list)
    assert "A" in result
    assert "B" not in result

def test_mark_feedback_nodes_sets_attribute():
    graph = nx.DiGraph()
    graph.add_nodes_from(["Node1", "Node2", "Node3"])
    sentinel_echo.mark_feedback_nodes(graph, ["Node1", "Node3"])

    assert graph.nodes["Node1"].get("feedback_hotspot") is True
    assert graph.nodes["Node3"].get("feedback_hotspot") is True
    assert graph.nodes["Node2"].get("feedback_hotspot") is None
