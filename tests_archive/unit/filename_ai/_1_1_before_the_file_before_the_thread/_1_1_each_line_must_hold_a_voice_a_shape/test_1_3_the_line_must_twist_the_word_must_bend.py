"""
tests/test_1_3_the_line_must_twist_the_word_must_bend.py

Tests the reshape_poetic_line function from filename_ai stanza
_1_3_the_line_must_twist_the_word_must_bend.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from storybook_fun_factory.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _1_3_the_line_must_twist_the_word_must_bend

def test_reshape_poetic_line():
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("a—dash—in—thought") == "a dash in thought"
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("“Curved quotes” and ‘single ones’") == '"Curved quotes" and \'single ones\''
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("…and the ellipsis appears") == "...and the ellipsis appears"
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("  leading and trailing   ") == "leading and trailing"
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("!!!Exclaim me!!!") == "Exclaim me"
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("") == ""
    assert _1_3_the_line_must_twist_the_word_must_bend.reshape_poetic_line("–hyphen–dash—mixed") == "hyphen dash mixed"
