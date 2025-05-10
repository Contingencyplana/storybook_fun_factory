"""
Test File: test_s8_3_it_tracks_the_names_and_maps_the_form.py

Tests the verse registry builder from High Command Cycle 4, Stanza 1, Line 3.
Follows 📜 5.5 and validates stanza metadata transformation.
"""

import os
import sys
import tempfile
import json
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer
HELPER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py"))
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the target module dynamically
MODULE_PATH = os.path.abspath(
    os.path.join(
        Path.cwd(),
        "game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s8_3_it_tracks_the_names_and_maps_the_form.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
build_verse_registry = module.build_verse_registry
TRACE_FILENAME = module.TRACE_FILENAME

def test_build_verse_registry_creates_correct_registry():
    with tempfile.TemporaryDirectory() as tmpdirname:
        trace_dir = Path(tmpdirname)
        trace_data = {
            "memory_ai": ["memory/s8_1_a_trace.py"],
            "visualizer": ["viz/s8_2_a_vision.py"]
        }

        # Write the trace file
        trace_path = trace_dir / TRACE_FILENAME
        with open(trace_path, "w", encoding="utf-8") as f:
            json.dump(trace_data, f, indent=2)

        registry = build_verse_registry(trace_dir)

        assert "s8_1_a_trace.py" in registry
        assert registry["s8_1_a_trace.py"]["component"] == "memory_ai"
        assert registry["s8_1_a_trace.py"]["path"] == "memory/s8_1_a_trace.py"

        assert "s8_2_a_vision.py" in registry
        assert registry["s8_2_a_vision.py"]["component"] == "visualizer"
        assert registry["s8_2_a_vision.py"]["path"] == "viz/s8_2_a_vision.py"
