"""
Filename: test_1_1_a_verse_is_born_but_cannot_live.py
(Tests for validating the poetic line's executable readiness in filename_ai)

This test suite checks latent vs. valid status for poetic lines
using dynamic import of s1_1_a_verse_is_born_but_cannot_live.py.
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
        "s1_1_a_verse_is_born_but_cannot_live.py",
    )
)

# Access the function
poetic_line_status = module.poetic_line_status


def test_poetic_line_status():
    assert poetic_line_status("The Light That Shaped the Sky") == "latent"
    assert poetic_line_status("a_whisper, shaped...") == "latent"
    assert poetic_line_status("  trailing_space  ") == "latent"
    assert poetic_line_status("the_light_that_shaped_the_sky") == "valid"
    assert poetic_line_status("whispered_rhythm_in_code") == "valid"
