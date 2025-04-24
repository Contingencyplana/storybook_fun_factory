# Filename: test_2_4_where_rhyme_and_rhythm_turn_to_run.py

import sys
import os
import pytest
import networkx as nx
import matplotlib
from pathlib import Path

# Prevent GUI issues
matplotlib.use("Agg")

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _2_4_where_rhyme_and_rhythm_turn_to_run as flowline


def test_animate_recursive_rhythm_accepts_valid_layouts(monkeypatch):
    graph = nx.DiGraph()
    graph.add_edge("A", "B")
    graph.add_node("C")

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    try:
        flowline.animate_recursive_rhythm(graph, layout="spring")
        flowline.animate_recursive_rhythm(graph, layout="circular")
        flowline.animate_recursive_rhythm(graph, layout="kamada_kawai")
    except Exception as e:
        pytest.fail(f"animate_recursive_rhythm failed with valid layouts: {e}")


def test_animate_recursive_rhythm_falls_back_to_default_on_invalid_layout(monkeypatch):
    graph = nx.DiGraph()
    graph.add_edge("X", "Y")

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    try:
        flowline.animate_recursive_rhythm(graph, layout="invalid_layout")
    except Exception as e:
        pytest.fail(f"Function did not fallback gracefully on invalid layout: {e}")


def test_animate_recursive_rhythm_saves_gif(tmp_path):
    graph = nx.DiGraph()
    graph.add_edge("1", "2")
    graph.add_edge("2", "3")
    output = tmp_path / "test_rhythm.gif"

    # Suppress display
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    flowline.animate_recursive_rhythm(graph, layout="spring", save_path=output)
    assert output.exists(), "GIF output not created"
    assert output.stat().st_size > 0, "GIF file is empty"

    # Also save permanent version
    official_output = Path("visualizer_output/where_rhyme_and_rhythm_turn_to_run.gif")
    flowline.animate_recursive_rhythm(graph, layout="spring", save_path=official_output)
    assert official_output.exists(), "Permanent visualizer_output GIF not created"
