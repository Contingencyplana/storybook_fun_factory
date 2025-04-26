"""
test_2_1_if_something_fades_too_fast_too_far.py

Tests the functionality of detect_fading_recursion from
_2_1_if_something_fades_too_fast_too_far.py
"""

import pytest
from sentinel_ai.loopwatchers.recursion_monitors._2_1_if_something_fades_too_fast_too_far import detect_fading_recursion

def test_detect_fading_recursion_flags_fading_cycles():
    sample_cycles = [
        {'id': 'cycle_001', 'strength': 0.2, 'coherence': 0.4, 'age': 3},
        {'id': 'cycle_002', 'strength': 0.7, 'coherence': 0.8, 'age': 6},
        {'id': 'cycle_003', 'strength': 0.1, 'coherence': 0.2, 'age': 2},
    ]

    result = detect_fading_recursion(sample_cycles)
    faded_ids = [cycle['id'] for cycle in result]

    assert 'cycle_001' in faded_ids
    assert 'cycle_003' in faded_ids
    assert 'cycle_002' not in faded_ids

def test_detect_fading_recursion_returns_empty_when_no_fading():
    sample_cycles = [
        {'id': 'cycle_004', 'strength': 0.9, 'coherence': 0.95, 'age': 10},
        {'id': 'cycle_005', 'strength': 0.85, 'coherence': 0.9, 'age': 8},
    ]

    result = detect_fading_recursion(sample_cycles)
    assert result == []

def test_detect_fading_recursion_handles_missing_fields_gracefully():
    sample_cycles = [
        {'id': 'cycle_006'},  # Missing strength, coherence, age
        {'id': 'cycle_007', 'strength': 0.2},  # Partial data
    ]

    result = detect_fading_recursion(sample_cycles)
    faded_ids = [cycle['id'] for cycle in result]

    # Neither should be considered fading without full low values
    assert faded_ids == []
