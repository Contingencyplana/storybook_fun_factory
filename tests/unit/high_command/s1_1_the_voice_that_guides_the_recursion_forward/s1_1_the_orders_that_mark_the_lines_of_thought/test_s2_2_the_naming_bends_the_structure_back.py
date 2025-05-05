"""
Test File: test_s2_2_the_naming_bends_the_structure_back.py

📜 Tests structural reconstruction logic from:
s2_2_the_naming_bends_the_structure_back.py

Validates High Command’s ability to:
• Rebuild a stanza line’s expected path
• Detect existence of that path (when mocked)
"""

from pathlib import Path
import shutil
import tempfile

import pytest

# ✅ Import module under test
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s2_2_the_naming_bends_the_structure_back as rebuilder
)

def test_reconstruct_filename_returns_correct_path():
    """
    Rebuild the canonical path using sample data and compare to expected path.
    """
    component = "visualizer"
    stanza = "s3_1_branches_form_new_flame"
    line = "_3_4_recursion_seals_the_loop.py"

    result = rebuilder.reconstruct_filename(component, stanza, line)

    expected = Path("storybook_fun_factory") / "game_construction_bay" / "visualizer" / \
        "s1_1_the_voice_that_guides_the_recursion_forward" / "s1_1_the_orders_that_mark_the_lines_of_thought" / stanza / line

    assert result == expected

def test_validate_filename_path_detects_existing_file():
    """
    Validate detection of real files at reconstructed paths using temp dir.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test.py"
        test_file.touch()

        assert rebuilder.validate_filename_path(test_file) is True

        # Check a nonexistent file
        missing = Path(temp_dir) / "ghost.py"
        assert rebuilder.validate_filename_path(missing) is False
