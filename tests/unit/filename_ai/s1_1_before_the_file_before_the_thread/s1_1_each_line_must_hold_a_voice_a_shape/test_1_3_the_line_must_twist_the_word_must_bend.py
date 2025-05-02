"""
Filename: test_1_3_the_line_must_twist_the_word_must_bend.py
(Tests for reshaping malformed poetic input into normalized form)

This suite validates symbol, punctuation, and formatting normalization
from s1_3_the_line_must_twist_the_word_must_bend.py using dynamic import.
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
        "s1_3_the_line_must_twist_the_word_must_bend.py",
    )
)

# Access the function
reshape_poetic_line = module.reshape_poetic_line


def test_reshape_poetic_line():
    assert reshape_poetic_line("a—dash—in—thought") == "a dash in thought"
    assert reshape_poetic_line("“Curved quotes” and ‘single ones’") == '"Curved quotes" and \'single ones\''
    assert reshape_poetic_line("…and the ellipsis appears") == "...and the ellipsis appears"
    assert reshape_poetic_line("  leading and trailing   ") == "leading and trailing"
    assert reshape_poetic_line("!!!Exclaim me!!!") == "Exclaim me"
    assert reshape_poetic_line("") == ""
    assert reshape_poetic_line("–hyphen–dash—mixed") == "hyphen dash mixed"
