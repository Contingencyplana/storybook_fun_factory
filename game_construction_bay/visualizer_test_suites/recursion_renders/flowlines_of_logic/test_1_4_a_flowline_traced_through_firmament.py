# Filename: test_1_4_a_flowline_traced_through_firmament.py

import sys
import os
import pytest

# 👇 Add storybook_fun_factory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../../../../.."))

from game_construction_bay.visualizer.recursion_renders.flowlines_of_logic import _1_4_a_flowline_traced_through_firmament as flowline

@pytest.fixture
def output_path(tmp_path):
    return tmp_path / "test_output_1_4.png"

def test_draw_complete_flowline_creates_file(output_path):
    # Primary test: Save to a temporary path
    flowline.draw_complete_flowline(output_path=output_path)

    # Assertions for tmp file
    assert output_path.exists(), "The flowline image file was not created."
    assert output_path.stat().st_size > 0, "The generated image file is empty."

    # ALSO save to visualizer_output/ for permanent record
    official_path = "visualizer_output/a_flowline_traced_through_firmament.png"
    flowline.draw_complete_flowline(output_path=official_path)
    assert os.path.exists(official_path), "Official visualizer_output image was not created."
