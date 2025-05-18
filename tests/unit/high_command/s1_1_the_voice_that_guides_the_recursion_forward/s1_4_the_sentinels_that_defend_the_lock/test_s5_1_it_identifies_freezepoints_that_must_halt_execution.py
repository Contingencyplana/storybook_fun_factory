"""
test_s5_1_it_identifies_freezepoints_that_must_halt_execution.py

Tests logic for detecting freeze-worthy recursion anomalies.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s5_1_it_identifies_freezepoints_that_must_halt_execution as freezer

def test_detects_freezepoint_above_threshold():
    anomalies = [
        {"id": "x1", "severity": 5},
        {"id": "x2", "severity": 9}
    ]
    result = freezer.identify_freezepoints(anomalies)
    assert len(result) == 1
    assert result[0]["id"] == "x2"

def test_all_freezepoints_if_all_above():
    anomalies = [
        {"id": "a", "severity": 8},
        {"id": "b", "severity": 10},
        {"id": "c", "severity": 7}
    ]
    result = freezer.identify_freezepoints(anomalies)
    assert len(result) == 3

def test_none_if_below_threshold():
    anomalies = [
        {"id": "y1", "severity": 2},
        {"id": "y2", "severity": 4}
    ]
    result = freezer.identify_freezepoints(anomalies)
    assert result == []

def test_custom_threshold_logic():
    anomalies = [
        {"id": "t1", "severity": 6},
        {"id": "t2", "severity": 7},
        {"id": "t3", "severity": 8}
    ]
    result = freezer.identify_freezepoints(anomalies, threshold=8)
    assert len(result) == 1
    assert result[0]["id"] == "t3"
