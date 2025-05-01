"""
Filename: test_s2_2_where_stanza_breath_and_syntax_dwell.py

Tests the style_poetic_filename function from filename_ai stanza
_s2_2_where_stanza_breath_and_syntax_dwell.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from storybook_fun_factory.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _2_2_where_stanza_breath_and_syntax_dwell

def test_style_poetic_filename():
    fn = _2_2_where_stanza_breath_and_syntax_dwell.style_poetic_filename

    assert fn("a_name_that_goes_on_and_on_forever.py") == "a_name_that_goes__on_and_on_forever.py"
    assert fn("___layered__underscore__mess.py") == "layered_underscore_mess.py"
    assert fn("__leading_and_trailing__.py") == "leading_and_trailing.py"
    assert fn("four_words_fit_exactly.py") == "four_words_fit_exactly.py"
    assert fn("five_words_need_breaking_up.py") == "five_words_need_breaking__up.py"
    assert fn("") == "unnamed_file"
