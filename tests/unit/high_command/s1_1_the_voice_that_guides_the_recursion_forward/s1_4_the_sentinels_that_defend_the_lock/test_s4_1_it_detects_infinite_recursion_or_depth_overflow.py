"""
test_s4_1_it_detects_infinite_recursion_or_depth_overflow.py

Tests the infinite recursion detection logic.
"""

import pytest
from game_construction_bay.high_command.s1_4_the_sentinels_that_defend_the_lock.cycle_2_anomaly_detection_and_freezepoints import s4_1_it_detects_infinite_recursion_or_depth_overflow as detector

def test_detects_overflow_above_threshold():
    assert detector.detect_infinite_recursion(1500) is True

def test_does_not_flag_below_threshold():
    assert detector.detect_infinite_recursion(500) is False

def test_threshold_can_be_customized():
    assert detector.detect_infinite_recursion(120, max_depth=100) is True
    assert detector.detect_infinite_recursion(80, max_depth=100) is False
