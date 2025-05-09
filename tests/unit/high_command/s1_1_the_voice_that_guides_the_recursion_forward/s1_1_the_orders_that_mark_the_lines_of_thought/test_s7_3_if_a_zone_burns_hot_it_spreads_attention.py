"""
Test File: test_s7_3_if_a_zone_burns_hot_it_spreads_attention.py

Dynamically tests the detect_hot_zones function from s7_3_if_a_zone_burns_hot_it_spreads_attention.py
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
    "s7_3_if_a_zone_burns_hot_it_spreads_attention.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

# ✅ Access the function to test
detect_hot_zones = module.detect_hot_zones

def test_detects_hot_zones_based_on_recent_activity():
    now = datetime.now(timezone.utc)
    recent = [(now - timedelta(minutes=i)).isoformat() for i in (5, 10, 15)]
    older = [(now - timedelta(hours=2)).isoformat()]

    zone_activity = {
        "zone_a": recent,
        "zone_b": older,
        "zone_c": recent + [(now - timedelta(minutes=1)).isoformat()],
    }

    result = detect_hot_zones(zone_activity, recent_window_minutes=30, activity_threshold=3)
    assert "zone_a" in result
    assert "zone_c" in result
    assert "zone_b" not in result

def test_returns_empty_when_no_hot_zones():
    now = datetime.now(timezone.utc)
    timestamps = [(now - timedelta(minutes=40)).isoformat()] * 5

    zone_activity = {
        "zone_a": timestamps,
        "zone_b": [],
    }

    result = detect_hot_zones(zone_activity, recent_window_minutes=30, activity_threshold=3)
    assert result == []

def test_ignores_invalid_timestamps_gracefully():
    now = datetime.now(timezone.utc)
    zone_activity = {
        "zone_a": ["not-a-time", now.isoformat(), (now - timedelta(minutes=2)).isoformat()],
        "zone_b": ["not-a-time", "also-invalid"]
    }

    result = detect_hot_zones(zone_activity, recent_window_minutes=10, activity_threshold=2)
    assert "zone_a" in result
    assert "zone_b" not in result
