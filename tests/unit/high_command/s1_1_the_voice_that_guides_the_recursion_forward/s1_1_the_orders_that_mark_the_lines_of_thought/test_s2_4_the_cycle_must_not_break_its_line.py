"""
Test File: test_s2_4_the_cycle_must_not_break_its_line.py

📜 Tests the stanza cycle validation logic in:
s2_4_the_cycle_must_not_break_its_line.py

Ensures that High Command:
• Accepts only valid 4-line stanza cycles
• Flags malformed or incomplete stanza sets
"""

from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s2_4_the_cycle_must_not_break_its_line as validator
)

def test_valid_cycle_passes():
    stanza = [
        "_2_1_a_single_breath_declares.py",
        "_2_2_a_second_form_resolves.py",
        "_2_3_a_third_path_bends.py",
        "_2_4_a_fourth_loop_closes.py"
    ]
    assert validator.is_valid_stanza_cycle(stanza)

def test_incomplete_cycle_fails():
    stanza = [
        "_2_1_a_single_breath_declares.py",
        "_2_2_a_second_form_resolves.py",
        "_2_3_a_third_path_bends.py"
    ]
    assert not validator.is_valid_stanza_cycle(stanza)

def test_malformed_names_fail():
    stanza = [
        "2_1_incorrect_name.py",
        "_2_2_a_second_form_resolves.py",
        "_2_a_third_path_bends.py",
        "_2_4_a_fourth_loop_closes.txt"
    ]
    assert not validator.is_valid_stanza_cycle(stanza)
