"""
Filename: test_1_4_to_meet_the_code_yet_not_transcend.py
(Tests for final filename syntax validation logic in filename_ai)

This suite ensures filename strings conform to all recursive naming rules
from s1_4_to_meet_the_code_yet_not_transcend.py using dynamic import.
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
        "s1_4_to_meet_the_code_yet_not_transcend.py",
    )
)

# Access the function
validate_final_filename = module.validate_final_filename


def test_validate_final_filename():
    # Valid cases
    assert validate_final_filename("a_valid_filename.py")
    assert validate_final_filename("poetic_slug_case.py")
    assert validate_final_filename("x1_y2_z3.py")

    # Invalid endings
    assert not validate_final_filename("missing_extension")
    assert not validate_final_filename("wrong.txt")

    # Invalid characters
    assert not validate_final_filename("camelCase.py")
    assert not validate_final_filename("has-dash.py")
    assert not validate_final_filename("has space.py")
    assert not validate_final_filename("semi;colon.py")

    # Structure violations
    assert not validate_final_filename("_starts_with_underscore.py")
    assert not validate_final_filename("ends_with_underscore_.py")
    assert not validate_final_filename("double__underscore.py")

    # Reserved words
    assert not validate_final_filename("def.py")
    assert not validate_final_filename("class.py")

    # Excessive length
    long_name = "a_" * 51 + "x.py"  # 102 chars including .py
    assert not validate_final_filename(long_name)
