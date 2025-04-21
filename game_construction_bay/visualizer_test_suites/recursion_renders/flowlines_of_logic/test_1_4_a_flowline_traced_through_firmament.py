# Filename: test_1_4_a_flowline_traced_through_firmament.py

import os
import pytest
from visualizer.recursion_renders.flowlines_of_logic import _1_4_a_flowline_traced_through_firmament as flowline

@pytest.fixture
def output_path(tmp_path):
    return tmp_path / "test_output.png"

def test_draw_complete_flowline_creates_file(output_path):
    # Run the visualization function
    flowline.draw_complete_flowline(output_path=output_path)

    # Assert the file was created
    assert output_path.exists(), "The flowline image file was not created."

    # Assert file is non-empty
    assert output_path.stat().st_size > 0, "The generated image file is empty."
