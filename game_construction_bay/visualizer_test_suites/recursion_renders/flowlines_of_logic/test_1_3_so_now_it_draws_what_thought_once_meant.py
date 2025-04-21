# test_1_3_so_now_it_draws_what_thought_once_meant.py

import pytest
from pathlib import Path

# Define expected output location
OUTPUT_DIR = Path("visualizer_output")
OUTPUT_FILE = OUTPUT_DIR / "so_now_it_draws_what_thought_once_meant.png"

def test_output_file_creation():
    # Remove file if it already exists
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    # Import the target module to trigger graph rendering
    import storybook_fun_factory.visualizer._1_1_not_every_thread_is_seen_or_told._1_1_it_starts_with_one_then_splits_in_two._1_3_so_now_it_draws_what_thought_once_meant

    # Confirm output was created
    assert OUTPUT_DIR.exists(), "Output directory was not created."
    assert OUTPUT_FILE.exists(), "Expected output PNG file was not created."
    assert OUTPUT_FILE.stat().st_size > 0, "Output file is empty."
