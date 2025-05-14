"""
Test File: test_s7_1_if_a_zone_fails_twice_it_signals_alert.py

Dynamically tests the flag_repeated_failures function from s7_1_if_a_zone_fails_twice_it_signals_alert.py
in accordance with 📜 5.5 – Dynamic Import Test Methodology.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the target stanza module from game_construction_bay
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s7_1_if_a_zone_fails_twice_it_signals_alert.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

# ✅ Access the function to test
flag_repeated_failures = module.flag_repeated_failures

def test_flag_repeated_failures_detects_multiple_failures():
    zone_history = {
        "zone_a": ["failing", "testing", "failing"],
        "zone_b": ["creative", "failing", "creative"],
        "zone_c": ["failing", "failing", "failing"],
        "zone_d": ["testing", "creative", "creative"]
    }

    result = flag_repeated_failures(zone_history)
    assert "zone_a" in result
    assert "zone_c" in result
    assert "zone_b" not in result
    assert "zone_d" not in result

def test_flag_repeated_failures_empty_history():
    zone_history = {}
    result = flag_repeated_failures(zone_history)
    assert result == []

def test_flag_repeated_failures_no_failing_zones():
    zone_history = {
        "zone_a": ["creative", "creative"],
        "zone_b": ["testing", "creative"]
    }

    result = flag_repeated_failures(zone_history)
    assert result == []
