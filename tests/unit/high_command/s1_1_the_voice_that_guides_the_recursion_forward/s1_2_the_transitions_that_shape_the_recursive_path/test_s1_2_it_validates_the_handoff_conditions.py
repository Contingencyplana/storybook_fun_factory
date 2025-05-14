"""
Test File: test_s1_2_it_validates_the_handoff_conditions.py

Tests the validation logic of recursive handoff preconditions.
Follows Dynamic Import Methodology as per 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer from correct helper path
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Import the main module dynamically from game_construction_bay
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_2_the_transitions_that_shape_the_recursive_path",
    "s1_2_it_validates_the_handoff_conditions.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_all_conditions_valid():
    context = {
        "loop_closed": True,
        "name_format_valid": True,
        "memory_registered": True,
        "log_complete": True
    }
    assert module.validate_handoff_conditions(context) is True

def test_missing_loop_closure():
    context = {
        "loop_closed": False,
        "name_format_valid": True,
        "memory_registered": True,
        "log_complete": True
    }
    assert module.validate_handoff_conditions(context) is False

def test_missing_memory_registry():
    context = {
        "loop_closed": True,
        "name_format_valid": True,
        "memory_registered": False,
        "log_complete": True
    }
    assert module.validate_handoff_conditions(context) is False

def test_missing_log():
    context = {
        "loop_closed": True,
        "name_format_valid": True,
        "memory_registered": True,
        "log_complete": False
    }
    assert module.validate_handoff_conditions(context) is False
