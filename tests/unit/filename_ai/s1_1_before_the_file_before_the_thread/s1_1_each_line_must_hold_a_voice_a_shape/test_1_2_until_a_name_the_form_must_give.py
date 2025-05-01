"""
Filename: test_s1_2_until_a_name_the_form_must_give.py

Tests the poetic_line_to_filename function from filename_ai stanza
_s1_2_until_a_name_the_form_must_give.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from storybook_fun_factory.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _1_2_until_a_name_the_form_must_give

def test_poetic_line_to_filename():
    assert _1_2_until_a_name_the_form_must_give.poetic_line_to_filename("a name that sings yet fits the tape") == "a_name_that_sings_yet_fits_the_tape.py"
    assert _1_2_until_a_name_the_form_must_give.poetic_line_to_filename("  no_slashes break no:colons bind ") == "no_slashes_break_nocolons_bind.py"
    assert _1_2_until_a_name_the_form_must_give.poetic_line_to_filename("A Line With CAPS and Spaces") == "a_line_with_caps_and_spaces.py"
    assert _1_2_until_a_name_the_form_must_give.poetic_line_to_filename("must-keep?it*safe|&clean!") == "mustkeepitsafeclean.py"
    assert _1_2_until_a_name_the_form_must_give.poetic_line_to_filename("") == "unnamed_line.py"
