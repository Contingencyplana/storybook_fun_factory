"""
Filename: test_1_2_until_a_name_the_form_must_give.py
(Tests for transforming poetic lines into valid Python filenames)

This suite verifies the poetic → filename transformation logic
in s1_2_until_a_name_the_form_must_give.py using dynamic import.
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
        "s1_2_until_a_name_the_form_must_give.py",
    )
)

# Access the function
poetic_line_to_filename = module.poetic_line_to_filename


def test_poetic_line_to_filename():
    assert poetic_line_to_filename("a name that sings yet fits the tape") == "a_name_that_sings_yet_fits_the_tape.py"
    assert poetic_line_to_filename("  no_slashes break no:colons bind ") == "no_slashes_break_nocolons_bind.py"
    assert poetic_line_to_filename("A Line With CAPS and Spaces") == "a_line_with_caps_and_spaces.py"
    assert poetic_line_to_filename("must-keep?it*safe|&clean!") == "mustkeepitsafeclean.py"
    assert poetic_line_to_filename("") == "unnamed_line.py"
