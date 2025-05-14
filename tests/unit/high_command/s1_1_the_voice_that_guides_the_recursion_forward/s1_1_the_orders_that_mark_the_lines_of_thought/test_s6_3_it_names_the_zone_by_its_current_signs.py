"""
Test File: test_s6_3_it_names_the_zone_by_its_current_signs.py
Tests the logic of s6_3_it_names_the_zone_by_its_current_signs.py
Ensures zone type assignment behaves as expected under various file conditions.
"""

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s6_3_it_names_the_zone_by_its_current_signs as classifier
)


def test_creative_zone():
    """Detects .md and .txt files as 'creative'."""
    files = ["intro.md", "notes.txt"]
    result = classifier.classify_zone(files)
    assert result == "creative"


def test_testing_zone():
    """Detects test_*.py patterns as 'testing'."""
    files = ["test_engine.py", "test_api.py"]
    result = classifier.classify_zone(files)
    assert result == "testing"


def test_failing_zone():
    """Detects zone with failure logs or 'fail' in filenames as 'failing'."""
    files = ["fail_log.txt", "test_fail_output.log"]
    result = classifier.classify_zone(files)
    assert result == "failing"


def test_stalled_zone():
    """Detects zone with unrelated or no informative files as 'stalled'."""
    files = ["script.py", "config.json"]
    result = classifier.classify_zone(files)
    assert result == "stalled"


def test_mixed_zone():
    """Tests prioritization of failing over testing and creative."""
    files = ["notes.md", "test_alpha.py", "error_log.txt"]
    result = classifier.classify_zone(files)
    assert result == "failing"  # Reflects priority logic


def test_assign_zone_types_bulk_classification():
    """Tests full assignment logic across multiple zones."""
    input_map = {
        "alpha": ["design.md"],
        "beta": ["test_api.py"],
        "gamma": ["fail_log.txt"],
        "delta": ["script.py"],
        "epsilon": ["fail.md", "test_fail.py", "logfile.log"]
    }
    expected = {
        "alpha": "creative",
        "beta": "testing",
        "gamma": "failing",
        "delta": "stalled",
        "epsilon": "failing"  # Prioritizes 'failing' over others
    }
    result = classifier.assign_zone_types(input_map)
    assert result == expected
