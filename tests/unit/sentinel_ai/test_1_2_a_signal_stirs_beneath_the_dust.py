# Filename: test_1_2_a_signal_stirs_beneath_the_dust.py

import sys
import os
from pathlib import Path
import pytest
import networkx as nx

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath("src"))

from storybook_fun_factory.sentinel_ai._1_1_the_watchers_wake_with_silent_sight._1_1_they_track_recursions_crooked_flow import _1_2_a_signal_stirs_beneath_the_dust as sentinel_signal


def test_activate_latent_diagnostics_detects_latent_nodes():
    graph = nx.DiGraph()
    graph.add_nodes_from([
        ("A", {"latent_signal": True}),
        ("B", {}),
        ("C", {"latent_signal": True}),
        ("D", {})
    ])
    
    result = sentinel_signal.activate_latent_diagnostics(graph)
    
    assert isinstance(result, list)
    assert "A" in result
    assert "C" in result
    assert "B" not in result
    assert "D" not in result


def test_flag_activated_nodes_sets_attribute():
    graph = nx.DiGraph()
    graph.add_nodes_from(["X", "Y", "Z"])
    sentinel_signal.flag_activated_nodes(graph, ["X", "Z"])
    
    assert graph.nodes["X"].get("activated") is True
    assert graph.nodes["Z"].get("activated") is True
    assert graph.nodes["Y"].get("activated") is None
