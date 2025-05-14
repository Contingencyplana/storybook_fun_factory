"""
Test File: test_s1_1_it_detects_the_signal_of_departure.py

Tests the detection of a departure signal in recursive handoff logic.
Follows Dynamic Import Methodology as per 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer from canonical Core Ecosystem Map location
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically import target module from game_construction_bay
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_2_the_transitions_that_shape_the_recursive_path",
    "s1_1_it_detects_the_signal_of_departure.py",
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_detect_departure_signal_true():
    context = {"status": "ready_to_depart", "trace_id": "abc123"}
    assert module.detect_departure_signal(context) is True

def test_detect_departure_signal_false_due_to_status():
    context = {"status": "idle", "trace_id": "abc123"}
    assert module.detect_departure_signal(context) is False

def test_detect_departure_signal_false_due_to_missing_trace_id():
    context = {"status": "ready_to_depart"}
    assert module.detect_departure_signal(context) is False
