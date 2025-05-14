# Filename: test_s3_3_diagrams_fold_and_split_as_one.py

import sys
import os
import pytest
import networkx as nx
from pathlib import Path

# Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath("game_construction_bay"))

from visualizer.recursion_renders.flowlines_of_logic import _3_3_diagrams_fold_and_split_as_one as flowline


def test_build_fold_and_split_diagram_structure():
    graph = nx.DiGraph()
    inputs = ["In_A", "In_B"]
    fold_point = "Merge"
    outputs = ["Out_X", "Out_Y"]
    graph = flowline.build_fold_and_split_diagram(graph, inputs, fold_point, outputs)

    # Fold point
    assert fold_point in graph.nodes
    assert graph.nodes[fold_point]["type"] == "confluence"

    # Inputs
    for i in inputs:
        assert i in graph.nodes
        assert graph.nodes[i]["type"] == "input_branch"
        assert graph.has_edge(i, fold_point)
        assert graph.get_edge_data(i, fold_point)["type"] == "converges_into"

    # Outputs
    for o in outputs:
        assert o in graph.nodes
        assert graph.nodes[o]["type"] == "output_branch"
        assert graph.has_edge(fold_point, o)
        assert graph.get_edge_data(fold_point, o)["type"] == "splits_into"


def test_render_fold_and_split_diagram_saves_image(tmp_path):
    graph = nx.DiGraph()
    inputs = ["Top", "Bottom"]
    fold_point = "Center"
    outputs = ["Left", "Right"]
    graph = flowline.build_fold_and_split_diagram(graph, inputs, fold_point, outputs)

    # Temporary output check
    temp_path = tmp_path / "fold_split_temp.png"
    flowline.render_fold_and_split_diagram(graph, save_path=temp_path)
    assert temp_path.exists()
    assert temp_path.stat().st_size > 0

    # Official output check
    official_path = Path("visualizer_output/diagrams_fold_and_split_as_one.png")
    flowline.render_fold_and_split_diagram(graph, save_path=official_path)
    assert official_path.exists()
    assert official_path.stat().st_size > 0
