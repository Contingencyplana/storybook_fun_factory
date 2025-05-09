"""
Test File: test_s7_2_if_a_zone_sleeps_it_prods_for_motion.py

Dynamically tests the detect_stale_zones function from s7_2_if_a_zone_sleeps_it_prods_for_motion.py
in accordance with 📜 5.5 – Dynamic Import Test Methodology.
"""

import os
import importlib.util
import pytest
from datetime import datetime, timedelta, timezone

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
    "s7_2_if_a_zone_sleeps_it_prods_for_motion.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

# ✅ Access the function to test
detect_stale_zones = module.detect_stale_zones

def test_detects_stale_zones_correctly():
    now = datetime.now(timezone.utc)
    old = (now - timedelta(days=10)).isoformat()
    recent = (now - timedelta(days=2)).isoformat()

    zone_map = {
        "zone_a": old,
        "zone_b": recent,
        "zone_c": old
    }

    result = detect_stale_zones(zone_map, threshold_days=7)
    assert "zone_a" in result
    assert "zone_c" in result
    assert "zone_b" not in result

def test_handles_empty_map():
    result = detect_stale_zones({}, threshold_days=7)
    assert result == []

def test_ignores_invalid_timestamps():
    zone_map = {
        "zone_a": "not-a-date",
        "zone_b": "2025-05-09T02:00:00"
    }

    result = detect_stale_zones(zone_map, threshold_days=0)
    assert "zone_b" in result
    assert "zone_a" not in result
