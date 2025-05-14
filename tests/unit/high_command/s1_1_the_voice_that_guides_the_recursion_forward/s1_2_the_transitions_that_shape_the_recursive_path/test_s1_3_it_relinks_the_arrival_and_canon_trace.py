"""
Test File: test_s1_3_it_relinks_the_arrival_and_canon_trace.py

Tests the relinking of canonical trace logic for recursive transitions.
Follows Dynamic Import Methodology as per 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load target module dynamically
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_2_the_transitions_that_shape_the_recursive_path",
    "s1_3_it_relinks_the_arrival_and_canon_trace.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_relink_success():
    context = {
        "source_id": "abc123",
        "destination_id": "def456",
        "canon_log": []
    }
    result = module.relink_canon_trace(context)
    assert result["trace_established"] is True
    assert "abc123 -> def456" in result["canon_log"]

def test_relink_missing_source():
    context = {
        "destination_id": "def456",
        "canon_log": []
    }
    result = module.relink_canon_trace(context)
    assert result["trace_established"] is False

def test_relink_missing_destination():
    context = {
        "source_id": "abc123",
        "canon_log": []
    }
    result = module.relink_canon_trace(context)
    assert result["trace_established"] is False
