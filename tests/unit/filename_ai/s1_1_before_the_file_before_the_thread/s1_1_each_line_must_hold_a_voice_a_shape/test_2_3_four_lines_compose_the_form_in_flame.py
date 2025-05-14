"""
Filename: test_2_3_four_lines_compose_the_form_in_flame.py
(Tests for stanza-wide filename normalization in filename_ai)

This suite checks that filename lines are cleaned and harmonized
from s2_3_four_lines_compose_the_form_in_flame.py using dynamic import.
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
        "s2_3_four_lines_compose_the_form_in_flame.py",
    )
)

# Access the function
enforce_stanza_consistency = module.enforce_stanza_consistency


def test_enforce_stanza_consistency():
    input_filenames = [
        "  WHISPER__to__FLAME.py",
        "echo-chamber.py",
        "flame.song().py",
        "__Structure__Is___KEY__.PY",
        "invalid name with spaces",
        "already_good_filename.py",
    ]

    expected = [
        "whisper_to_flame.py",
        "echochamber.py",
        "flamesong.py",
        "structure_is_key.py",
        "invalid_name_with_spaces.py",
        "already_good_filename.py",
    ]

    assert enforce_stanza_consistency(input_filenames) == expected
