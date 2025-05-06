"""
Test File: test_s4_1_it_reads_the_lines_that_wait_to_be.py

Tests the functionality of s4_1_it_reads_the_lines_that_wait_to_be.py.
Ensures that pending stanza lines are correctly identified based on mock status input.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s4_1_it_reads_the_lines_that_wait_to_be as target


def test_read_pending_lines_returns_correct_files():
    mock_status = {
        "line_1.py": "[🔜 Not started]",
        "line_2.py": "[✅ Success!]",
        "line_3.py": "[🔜 Not started]",
        "line_4.py": "[⏳ In progress]",
    }

    result = target.read_pending_lines(mock_status)
    assert result == ["line_1.py", "line_3.py"]


def test_read_pending_lines_empty_result():
    mock_status = {
        "line_1.py": "[✅ Success!]",
        "line_2.py": "[⏳ In progress]",
    }

    result = target.read_pending_lines(mock_status)
    assert result == []


def test_read_pending_lines_custom_marker():
    mock_status = {
        "line_1.py": "[WAITING]",
        "line_2.py": "[✅ Success!]",
        "line_3.py": "[WAITING]",
    }

    result = target.read_pending_lines(mock_status, marker="[WAITING]")
    assert result == ["line_1.py", "line_3.py"]
