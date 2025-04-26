"""
test_2_1_if_something_fades_too_fast_too_far.py

Tests the functionality of detect_fading_recursion from
_2_1_if_something_fades_too_fast_too_far.py
"""

import sys
import os
import pytest
import importlib.util

# Force src/ onto sys.path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..", "src")))

# Dynamically import the production file
module_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../src/storybook_fun_factory/sentinel_ai/_1_1_the_watchers_wake_with_silent_sight/_1_1_they_track_recursions_crooked_flow/_2_1_if_something_fades_too_fast_too_far.py"
    )
)

spec = importlib.util.spec_from_file_location("dynamic_module", module_path)
dynamic_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_module)

detect_fading_recursion = dynamic_module.detect_fading_recursion

# Tests start below
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

    assert faded_ids == []
