"""
Test File: test_s6_4_it_builds_the_map_that_keeps_track_of_flow.py
Tests the logic of s6_4_it_builds_the_map_that_keeps_track_of_flow.py
Ensures zone classification map is correctly generated from simulated activity logs.
"""

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s6_4_it_builds_the_map_that_keeps_track_of_flow as zone_mapper
)


def test_build_zone_type_map_basic():
    """Tests a basic mapping from file activity to classified zone types."""
    input_activity_log = {
        "alpha": ["design.md"],
        "beta": ["test_feature.py"],
        "gamma": ["fail_report.log"],
        "delta": ["script.py"],
        "epsilon": ["test_case.py", "fail.md"]
    }

    expected = {
        "alpha": "creative",
        "beta": "testing",
        "gamma": "failing",
        "delta": "stalled",
        "epsilon": "failing"  # failing takes precedence
    }

    result = zone_mapper.build_zone_type_map(input_activity_log)
    assert result == expected


def test_build_zone_type_map_empty():
    """Returns an empty result if activity log is empty."""
    result = zone_mapper.build_zone_type_map({})
    assert result == {}


def test_classification_prioritization():
    """Checks that classification always prioritizes correctly."""
    mixed_input = {
        "mixed1": ["fail.txt", "test_model.py", "notes.md"],
        "mixed2": ["test_utils.py", "readme.md"],
        "mixed3": ["manual.md", "thoughts.txt"]
    }

    result = zone_mapper.build_zone_type_map(mixed_input)

    assert result["mixed1"] == "failing"
    assert result["mixed2"] == "testing"
    assert result["mixed3"] == "creative"
