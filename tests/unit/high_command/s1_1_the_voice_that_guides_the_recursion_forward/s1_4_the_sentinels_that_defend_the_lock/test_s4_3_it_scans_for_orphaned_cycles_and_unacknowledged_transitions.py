"""
test_s4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py

Tests for detecting orphaned cycles and unacknowledged transitions.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions as scanner

def test_detects_orphan_and_unacknowledged_cycles():
    trace_log = [
        {'id': 's1', 'parent_id': 'root', 'acknowledged': True},
        {'id': 's2', 'parent_id': None, 'acknowledged': True},         # Orphaned
        {'id': 's3', 'parent_id': 's1', 'acknowledged': False},        # Unacknowledged
        {'id': 's4', 'parent_id': 's2', 'acknowledged': False}         # Both
    ]
    result = scanner.scan_for_orphaned_cycles_and_transitions(trace_log)
    assert len(result) == 3
    assert {'id': 's2', 'parent_id': None, 'acknowledged': True} in result
    assert {'id': 's3', 'parent_id': 's1', 'acknowledged': False} in result
    assert {'id': 's4', 'parent_id': 's2', 'acknowledged': False} in result

def test_passes_fully_valid_trace():
    trace_log = [
        {'id': 's1', 'parent_id': 'root', 'acknowledged': True},
        {'id': 's2', 'parent_id': 's1', 'acknowledged': True},
        {'id': 's3', 'parent_id': 's2', 'acknowledged': True}
    ]
    result = scanner.scan_for_orphaned_cycles_and_transitions(trace_log)
    assert result == []
