"""
Test File: test_s8_2_it_logs_the_lines_and_saves_the_trace.py

Tests the stanza trace logger from High Command Cycle 4, Stanza 1, Line 2.
Follows 📜 5.5 methodology and verifies persistence and data accuracy.
"""

import os
import sys
import tempfile
import importlib.util
from pathlib import Path
import json
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
        "game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s8_2_it_logs_the_lines_and_saves_the_trace.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
log_stanza_metadata_to_trace = module.log_stanza_metadata_to_trace
TRACE_FILENAME = module.TRACE_FILENAME

def test_log_stanza_metadata_to_trace_creates_correct_file():
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_dir = Path(tmpdirname)
        mock_metadata = {
            "dream_journal": ["s1_1_echo_awakens.py", "s1_2_trace_deepens.py"],
            "filename_ai": ["s2_1_naming_logic.py"]
        }

        trace_path = log_stanza_metadata_to_trace(mock_metadata, output_dir)

        # Validate path
        assert trace_path.name == TRACE_FILENAME
        assert trace_path.exists()

        # Validate content
        with open(trace_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data == mock_metadata
