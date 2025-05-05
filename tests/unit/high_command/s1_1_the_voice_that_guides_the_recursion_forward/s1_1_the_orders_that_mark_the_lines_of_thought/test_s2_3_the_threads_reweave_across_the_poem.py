"""
Test File: test_s2_3_the_missing_must_be_named_to_be_found.py

📜 Tests the identification logic in:
s2_3_the_missing_must_be_named_to_be_found.py

Verifies that High Command correctly identifies missing stanza lines
from a canonical list when compared to currently existing filenames.
"""

from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s2_3_the_missing_must_be_named_to_be_found as finder
)

def test_identifies_missing_lines():
    expected = [
        "_1_1_a_first_breath.py",
        "_1_2_a_second_shape.py",
        "_1_3_a_third_spark.py",
        "_1_4_a_fourth_thread.py"
    ]
    existing = [
        "_1_1_a_first_breath.py",
        "_1_3_a_third_spark.py"
    ]
    result = finder.identify_missing_lines(expected, existing)

    assert result == [
        "_1_2_a_second_shape.py",
        "_1_4_a_fourth_thread.py"
    ]

def test_returns_empty_when_all_present():
    expected = [
        "_1_1_a_first_breath.py",
        "_1_2_a_second_shape.py"
    ]
    existing = [
        "_1_1_a_first_breath.py",
        "_1_2_a_second_shape.py"
    ]
    result = finder.identify_missing_lines(expected, existing)
    assert result == []
