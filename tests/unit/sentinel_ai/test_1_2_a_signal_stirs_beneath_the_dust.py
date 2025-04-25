# Filename: test_1_2_a_signal_stirs_beneath_the_dust.py

import sys
import os
from pathlib import Path
import pytest
import networkx as nx

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath("src"))

from storybook_fun_factory.sentinel_ai._1_1_the_watchers_wake_with_silent_sight._1_1_they_track_recursions_crooked_flow import _1_2_a_signal_stirs_beneath_the_dust as sentinel_signal


def test_activate_latent_signals_detects_low_recursion_nodes():
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("A", "A"),  # Self-loop
        ("B", "C"),  # Minimal non-recursive connection
        ("D", "D")   # Another self-loop
    ])
    
    result = sentinel_signal.activate_latent_signals(graph, dust_threshold=1)
    
    assert isinstance(result, list)
    assert "A" in result
    assert "D" in result
    assert "B" not in result  # No recursion detected at B


def test_mark_latent_signals_on_graph_sets_flag():
    graph = nx.DiGraph()
    graph.add_nodes_from(["A", "B", "C"])
    sentinel_signal.mark_latent_signals_on_graph(graph, ["A", "C"])
    
    assert graph.nodes["A"].get("latent_signal") is True
    assert graph.nodes["C"].get("latent_signal") is True
    assert graph.nodes["B"].get("latent_signal") is None


def test_render_latent_signal_graph_saves_file(tmp_path):
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("N1", "N1"),
        ("N2", "N3"),
        ("N3", "N2"),
    ])
    sentinel_signal.mark_latent_signals_on_graph(graph, ["N1"])
    output_path = tmp_path / "test_latent_signal_output.png"
    
    sentinel_signal.render_latent_signal_graph(graph, save_path=output_path)
    
    assert output_path.exists()
    assert output_path.stat().st_size > 0
