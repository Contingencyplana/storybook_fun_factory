# Filename: test_s3_2_in_choice_and_echo_the_shapes_do_show.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to the path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _3_2_in_choice_and_echo_the_shapes_do_show as flowline


def test_build_choice_echo_graph_structure():
    graph = nx.DiGraph()
    root = "Decision"
    choices = [
        ("A", "A_echo"),
        ("B", "B_echo")
    ]
    graph = flowline.build_choice_echo_graph(graph, root, choices)

    # Root node
    assert root in graph.nodes
    assert graph.nodes[root]["type"] == "decision_root"

    # Choices and echoes
    for choice, echo in choices:
        assert choice in graph.nodes
        assert echo in graph.nodes

        assert graph.nodes[choice]["type"] == "choice"
        assert graph.nodes[echo]["type"] == "echo"

        assert graph.has_edge(root, choice)
        assert graph.get_edge_data(root, choice)["type"] == "choice_path"

        assert graph.has_edge(choice, echo)
        assert graph.get_edge_data(choice, echo)["type"] == "echo_reflection"


def test_render_choice_echo_graph_creates_image(tmp_path):
    graph = nx.DiGraph()
    choices = [
        ("Yes", "Yes_Return"),
        ("No", "No_Return")
    ]
    graph = flowline.build_choice_echo_graph(graph, root="RootNode", choices=choices)

    # Temporary image output
    tmp_output = tmp_path / "temp_choice_echo.png"
    flowline.render_choice_echo_graph(graph, save_path=tmp_output)
    assert tmp_output.exists()
    assert tmp_output.stat().st_size > 0

    # Official image output
    official_output = Path("visualizer_output/in_choice_and_echo_the_shapes_do_show.png")
    flowline.render_choice_echo_graph(graph, save_path=official_output)
    assert official_output.exists()
    assert official_output.stat().st_size > 0
