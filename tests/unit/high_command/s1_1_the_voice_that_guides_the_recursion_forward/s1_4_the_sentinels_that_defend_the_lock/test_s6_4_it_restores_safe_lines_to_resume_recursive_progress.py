"""
Filename: test_s6_4_it_restores_safe_lines_to_resume_recursive_progress.py

Tests controlled restoration logic for validated stanza proposals.
Verifies:
- Only fully valid stanzas are restored
- Files are written to correct output folder
- Logs are appended per restoration
"""

import os
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s6_4_it_restores_safe_lines_to_resume_recursive_progress as restorer
)

@pytest.fixture
def validated_stanza_inputs():
    return [
        {
            "filename": "s6_4_valid_stanza_proper_name",
            "restored_content": "def valid():\n    return True",
            "source": "memory_ai",
            "path": "game_construction_bay/component/s6_4_valid_stanza_proper_name",
            "codex_valid": True,
            "filename_valid": True
        },
        {
            "filename": "s6_4_invalid_stanza_structure",
            "restored_content": "eval('nope')",
            "source": "archivist_ai",
            "path": "game_construction_bay/component/s6_4_invalid_stanza_structure",
            "codex_valid": False,
            "filename_valid": True
        },
        {
            "filename": "bad_naming",
            "restored_content": "def okay():\n    pass",
            "source": "memory_ai",
            "path": "game_construction_bay/component/bad_naming",
            "codex_valid": True,
            "filename_valid": False
        }
    ]

@pytest.fixture
def clean_restore_directory():
    temp_dir = tempfile.mkdtemp()
    restore_dir = Path(temp_dir) / "restored_lines"
    os.makedirs(restore_dir, exist_ok=True)

    original_dir = restorer.RESTORE_DIR
    original_log = restorer.RESTORE_LOG

    restorer.RESTORE_DIR = str(restore_dir)
    restorer.RESTORE_LOG = str(restore_dir / "restore_log.txt")

    yield restore_dir

    # Clean up and restore constants
    restorer.RESTORE_DIR = original_dir
    restorer.RESTORE_LOG = original_log
    rmtree(temp_dir)

def test_restore_safe_stanzas(validated_stanza_inputs, clean_restore_directory):
    restored = restorer.restore_safe_stanzas(validated_stanza_inputs)

    assert len(restored) == 1
    file_path = restored[0]
    assert os.path.exists(file_path)
    assert file_path.endswith("s6_4_valid_stanza_proper_name.py")

    log_file = clean_restore_directory / "restore_log.txt"
    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as log:
        contents = log.read()
        assert "s6_4_valid_stanza_proper_name" in contents
        assert "restored_to" in contents
