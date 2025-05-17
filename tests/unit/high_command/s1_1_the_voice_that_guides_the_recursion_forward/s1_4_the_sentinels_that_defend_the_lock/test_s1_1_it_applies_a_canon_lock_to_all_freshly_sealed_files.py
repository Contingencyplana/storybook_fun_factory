"""
test_s1_1_it_applies_a_canon_lock_to_all_freshly_sealed_files.py

Tests the canon lock application system for enforcement of
read-only status and lock metadata creation.

Compliant with 📜 5.5 – Dynamic Import Methodology
"""

import pytest
import tempfile
import os
import json
from pathlib import Path
from importlib import import_module

MODULE_PATH = "game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s1_1_it_applies_a_canon_lock_to_all_freshly_sealed_files"
MODULE_NAME = MODULE_PATH.split(".")[-1]

@pytest.fixture
def temp_poem_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test_poem.py"
        file_path.write_text("print('This is a stanza.')", encoding="utf-8")
        yield file_path
        # File and tempdir are auto-cleaned

def test_applies_canon_lock_creates_metadata_and_locks_file(temp_poem_file):
    module = import_module(MODULE_PATH)
    apply_canon_lock = getattr(module, "apply_canon_lock")

    metadata = apply_canon_lock(str(temp_poem_file))

    # Check file is read-only
    assert not os.access(temp_poem_file, os.W_OK), "File should be read-only after locking."

    # Check lock metadata file exists
    lock_file = temp_poem_file.parent / ".canon_lock"
    assert lock_file.exists(), ".canon_lock file was not created."

    # Check lock file content
    with lock_file.open("r", encoding="utf-8") as f:
        content = json.load(f)

    assert any(entry["filename"] == temp_poem_file.name for entry in content), \
        "Lock metadata does not include the locked file."

    # Validate metadata structure
    assert "sha256" in metadata
    assert "timestamp" in metadata
    assert metadata["filename"] == temp_poem_file.name
