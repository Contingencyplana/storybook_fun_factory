"""
Test File: test_s7_1_if_a_zone_fails_twice_it_signals_alert.py

Tests the logic of flag_repeated_failures from s7_1_if_a_zone_fails_twice_it_signals_alert.py,
ensuring that zones with two or more 'failing' entries are correctly flagged for alert.
"""

import pytest
from storybook_fun_factory.high_command.s1_1_the_orders_that_mark_the_lines_of_thought.s7_1_if_a_zone_fails_twice_it_signals_alert import flag_repeated_failures

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
