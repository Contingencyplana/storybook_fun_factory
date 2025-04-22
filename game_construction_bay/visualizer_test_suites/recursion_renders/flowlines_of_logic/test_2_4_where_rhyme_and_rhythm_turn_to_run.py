# Filename: test_2_4_where_rhyme_and_rhythm_turn_to_run.py

import matplotlib
matplotlib.use("Agg")  # ✅ Prevent Tkinter errors by using a headless backend

import pytest
import networkx as nx

from visualizer.recursion_renders.flowlines_of_logic._2_4_where_rhyme_and_rhythm_turn_to_run import animate_recursive_rhythm

import pytest
import networkx as nx

from visualizer.recursion_renders.flowlines_of_logic._2_4_where_rhyme_and_rhythm_turn_to_run import animate_recursive_rhythm


def test_animate_recursive_rhythm_accepts_valid_layouts(monkeypatch):
    graph = nx.DiGraph()
    graph.add_edge("A", "B")
    graph.add_node("C")

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    try:
        animate_recursive_rhythm(graph, layout="spring")
        animate_recursive_rhythm(graph, layout="circular")
        animate_recursive_rhythm(graph, layout="kamada_kawai")
    except Exception as e:
        pytest.fail(f"animate_recursive_rhythm failed with valid layouts: {e}")


def test_animate_recursive_rhythm_falls_back_to_default_on_invalid_layout(monkeypatch):
    graph = nx.DiGraph()
    graph.add_edge("X", "Y")

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    try:
        animate_recursive_rhythm(graph, layout="invalid_layout")
    except Exception as e:
        pytest.fail(f"Function did not fallback gracefully on invalid layout: {e}")
