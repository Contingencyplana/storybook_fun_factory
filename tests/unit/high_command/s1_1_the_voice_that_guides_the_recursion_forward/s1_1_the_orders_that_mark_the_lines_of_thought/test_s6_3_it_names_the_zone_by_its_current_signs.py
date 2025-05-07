"""
Test File: test_s6_3_it_names_the_zone_by_its_current_signs.py
Tests the logic of s6_3_it_names_the_zone_by_its_current_signs.py
Verifies that zone types are correctly classified based on file content.
"""

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s6_3_it_names_the_zone_by_its_current_signs as classifier


def test_creative_zone():
    """Detects zone with .md or .txt files as 'creative'."""
    files = ["summary.md", "intro.txt"]
    result = classifier.classify_zone(files)
    assert result == "creative"


def test_testing_zone():
    """Detects zone with test_*.py files as 'testing'."""
    files = ["test_engine.py", "test_flow.py"]
    result = classifier.classify_zone(files)
    assert result == "testing"


def test_failing_zone():
    """Detects zone with failure logs or 'fail' in filenames as 'failing'."""
    files = ["fail_log.txt", "test_fail_output.log"]
    result = classifier.classify_zone(files)
    assert result == "failing"


def test_stalled_zone():
    """Detects empty or irrelevant file lists as 'stalled'."""
    files = ["main.py", "README"]
    result = classifier.classify_zone(files)
    assert result == "stalled"


def test_mixed_zone():
    """Detects presence of multiple types and returns 'mixed'."""
    files = ["notes.md", "test_alpha.py", "error_log.txt"]
    result = classifier.classify_zone(files)
    assert result == "mixed"


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
        "epsilon": "mixed"
    }
    result = classifier.assign_zone_types(input_map)
    assert result == expected
