# Filename: test_s1_2_its_curve_concealed_its_arc_set_free.py

import sys
import os
import pytest
import importlib
from pathlib import Path

# 👇 Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

# Define output location
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "its_curve_concealed_its_arc_set_free.png"

def test_output_file_creation():
    # Remove file if it already exists
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    # Dynamically import the correct module in its new location
    module = importlib.import_module(
        "visualizer.recursion_renders.flowlines_of_logic._1_2_its_curve_concealed_its_arc_set_free"
    )

    # Call the expected rendering function
    module.draw_hidden_curve(output_path=OUTPUT_FILE)

    # Assert the image was created and non-empty
    assert OUTPUT_DIR.exists(), "Output directory was not created."
    assert OUTPUT_FILE.exists(), "Expected output PNG file was not created."
    assert OUTPUT_FILE.stat().st_size > 0, "Output file is empty."
