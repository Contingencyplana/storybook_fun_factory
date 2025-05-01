# Filename: test_s1_4_a_flash_to_mark_recursions_name.py

import sys
import os
import importlib.util
from pathlib import Path
import pytest
import networkx as nx

# Dynamically load the target file
target_path = Path("src/storybook_fun_factory/sentinel_ai/_1_1_the_watchers_wake_with_silent_sight/_1_1_they_track_recursions_crooked_flow/_1_4_a_flash_to_mark_recursions_name.py").resolve()
spec = importlib.util.spec_from_file_location("_1_4_a_flash_to_mark_recursions_name", target_path)
sentinel_flare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sentinel_flare)


def test_finalize_sentinel_flare_marks_critical_nodes():
    graph = nx.DiGraph()
    graph.add_nodes_from(["NodeX", "NodeY", "NodeZ"])
    
    sentinel_flare.finalize_sentinel_flare(graph, ["NodeX", "NodeZ"])
    
    assert graph.nodes["NodeX"].get("sentinel_flare") is True
    assert graph.nodes["NodeZ"].get("sentinel_flare") is True
    assert graph.nodes["NodeY"].get("sentinel_flare") is None


def test_visualize_sentinel_flare_creates_output(tmp_path):
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("Alpha", "Beta"),
        ("Beta", "Gamma"),
        ("Gamma", "Alpha")
    ])
    sentinel_flare.finalize_sentinel_flare(graph, ["Alpha"])
    output_path = tmp_path / "sentinel_flare_visualization.png"
    
    sentinel_flare.visualize_sentinel_flare(graph, save_path=output_path)
    
    assert output_path.exists()
    assert output_path.stat().st_size > 0
