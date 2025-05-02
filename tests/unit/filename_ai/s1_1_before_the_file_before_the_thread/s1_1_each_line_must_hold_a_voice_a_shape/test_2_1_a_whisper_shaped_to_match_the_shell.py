"""
Filename: test_2_1_a_whisper_shaped_to_match_the_shell.py
(Tests for syntactic poetic slug formatting in filename_ai)

This suite ensures lyrical spacing and emphasis are structurally transformed
from s2_1_a_whisper_shaped_to_match_the_shell.py using dynamic import.
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
        "s2_1_a_whisper_shaped_to_match_the_shell.py",
    )
)

# Access the function
format_poetic_slug = module.format_poetic_slug


def test_format_poetic_slug():
    assert format_poetic_slug("the shell holds space and tone") == "the_shell_holds_space_and_tone"
    assert format_poetic_slug("  a     line     with   gaps  ") == "a_line_with_gaps"
    assert format_poetic_slug("emphasized__pause__line") == "emphasized__pause__line"
    assert format_poetic_slug("_leading and trailing_") == "leading_and_trailing"
    assert format_poetic_slug("") == "unnamed_slug"
