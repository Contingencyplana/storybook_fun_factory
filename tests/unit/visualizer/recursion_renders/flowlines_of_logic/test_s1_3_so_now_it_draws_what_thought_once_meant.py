# Filename: test_s1_3_so_now_it_draws_what_thought_once_meant.py

import sys
import os
import pytest
import importlib
from pathlib import Path

# 👇 Add game_construction_bay to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

# Define expected output location
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "so_now_it_draws_what_thought_once_meant.png"

def test_output_file_creation():
    # Remove file if it already exists
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    # Import and invoke the target visual function
    module = importlib.import_module(
        "visualizer.recursion_renders.flowlines_of_logic._1_3_so_now_it_draws_what_thought_once_meant"
    )

    module.draw_logical_reflection(output_path=OUTPUT_FILE)

    # Confirm output was created and valid
    assert OUTPUT_DIR.exists(), "Output directory was not created."
    assert OUTPUT_FILE.exists(), "Expected output PNG file was not created."
    assert OUTPUT_FILE.stat().st_size > 0, "Output file is empty."
