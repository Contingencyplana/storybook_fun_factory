# test_1_2_its_curve_concealed_its_arc_set_free.py

import pytest
from pathlib import Path
import importlib

# Define output location
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "its_curve_concealed_its_arc_set_free.png"

def test_output_file_creation():
    # Remove file if it already exists
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    # Import the target module to trigger execution
    import storybook_fun_factory.visualizer._1_1_not_every_thread_is_seen_or_told._1_1_it_starts_with_one_then_splits_in_two._1_2_its_curve_concealed_its_arc_set_free

    # Assert the image was created
    assert OUTPUT_DIR.exists(), "Output directory was not created."
    assert OUTPUT_FILE.exists(), "Expected output PNG file was not created."
    assert OUTPUT_FILE.stat().st_size > 0, "Output file is empty."
