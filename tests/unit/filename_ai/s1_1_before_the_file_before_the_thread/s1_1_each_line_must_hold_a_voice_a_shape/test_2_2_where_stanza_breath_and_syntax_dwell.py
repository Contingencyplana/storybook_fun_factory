"""
Filename: test_2_2_where_stanza_breath_and_syntax_dwell.py
(Tests for stylizing filename rhythm and structural spacing in filename_ai)

This suite verifies underscore normalization and stanzaic spacing
from s2_2_where_stanza_breath_and_syntax_dwell.py using dynamic import.
"""

import os
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza module under test
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "filename_ai",
        "s1_1_before_the_file_before_the_thread",
        "s1_1_each_line_must_hold_a_voice_a_shape",
        "s2_2_where_stanza_breath_and_syntax_dwell.py",
    )
)

# Access the function
style_poetic_filename = module.style_poetic_filename


def test_style_poetic_filename():
    fn = style_poetic_filename

    assert fn("a_name_that_goes_on_and_on_forever.py") == "a_name_that_goes__on_and_on_forever.py"
    assert fn("___layered__underscore__mess.py") == "layered_underscore_mess.py"
    assert fn("__leading_and_trailing__.py") == "leading_and_trailing.py"
    assert fn("four_words_fit_exactly.py") == "four_words_fit_exactly.py"
    assert fn("five_words_need_breaking_up.py") == "five_words_need_breaking__up.py"
    assert fn("") == "unnamed_file"
