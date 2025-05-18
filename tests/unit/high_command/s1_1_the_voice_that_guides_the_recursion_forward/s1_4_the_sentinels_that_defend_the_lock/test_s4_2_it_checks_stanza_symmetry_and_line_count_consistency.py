"""
test_s4_2_it_checks_stanza_symmetry_and_line_count_consistency.py

Tests stanza structure and line count verification.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s4_2_it_checks_stanza_symmetry_and_line_count_consistency as checker

def test_valid_stanza_structure():
    files = [
        's4_1_it_detects_infinite_recursion_or_depth_overflow.py',
        's4_2_it_checks_stanza_symmetry_and_line_count_consistency.py',
        's4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py',
        's4_4_it_logs_anomalies_without_halting_execution_yet.py'
    ]
    assert checker.check_stanza_symmetry(files) is True

def test_invalid_line_count():
    files = [
        's4_1_it_detects_infinite_recursion_or_depth_overflow.py',
        's4_2_it_checks_stanza_symmetry_and_line_count_consistency.py',
        's4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py'
    ]
    assert checker.check_stanza_symmetry(files) is False

def test_invalid_filename_pattern():
    files = [
        's4_1_it_detects_infinite_recursion_or_depth_overflow.py',
        's4_2_BAD_FILENAME.py',
        's4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py',
        's4_4_it_logs_anomalies_without_halting_execution_yet.py'
    ]
    assert checker.check_stanza_symmetry(files) is False
