"""
test_s1_3_it_detects_post_canon_edit_attempts_and_rejects.py

Tests detection of post-canon tampering based on recorded SHA-256 hash.

Compliant with 📜 5.5 – Dynamic Import Methodology
"""

import pytest
import json
import hashlib
from pathlib import Path
from importlib import import_module

MODULE_PATH = "game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s1_3_it_detects_post_canon_edit_attempts_and_rejects"

def sha256_of(file: Path) -> str:
    h = hashlib.sha256()
    with file.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

@pytest.fixture
def locked_file(tmp_path):
    file_path = tmp_path / "locked_line.py"
    file_path.write_text("print('Original canon line')", encoding="utf-8")

    lock_data = [
        {
            "filename": file_path.name,
            "timestamp": "2025-05-17T12:00:00Z",
            "sha256": sha256_of(file_path)
        }
    ]

    lock_file = tmp_path / ".canon_lock"
    with lock_file.open("w", encoding="utf-8") as f:
        json.dump(lock_data, f, indent=2)

    yield file_path

    lock_file.unlink(missing_ok=True)

def test_detects_unchanged_file_is_valid(locked_file):
    module = import_module(MODULE_PATH)
    verify = getattr(module, "verify_canon_integrity")
    assert verify(str(locked_file)) is True

def test_detects_modified_file_is_invalid(locked_file):
    module = import_module(MODULE_PATH)
    verify = getattr(module, "verify_canon_integrity")

    # Tamper with file
    locked_file.write_text("print('Tampered!')", encoding="utf-8")
    assert verify(str(locked_file)) is False
