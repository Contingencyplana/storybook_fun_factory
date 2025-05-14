# Filename: test_s1_4_a_flowline_traced_through_firmament.py

import sys
import os
import pytest

# ✅ Add game_construction_bay to Python path so `visualizer/` can be found
sys.path.insert(0, os.path.abspath("game_construction_bay"))

# ✅ Clean import from inside game_construction_bay/
from visualizer.recursion_renders.flowlines_of_logic import _1_4_a_flowline_traced_through_firmament as flowline

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
