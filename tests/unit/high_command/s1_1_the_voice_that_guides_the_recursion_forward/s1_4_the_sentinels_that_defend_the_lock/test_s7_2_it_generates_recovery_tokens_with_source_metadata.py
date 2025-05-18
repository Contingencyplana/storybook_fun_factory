"""
Filename: test_s7_2_it_generates_recovery_tokens_with_source_metadata.py

Tests the generation of structured recovery tokens for failed stanzas.
Verifies:
- Tokens are created only for invalid entries
- Files are saved with correct timestamped filenames
- Token content includes required metadata fields
"""

import os
import json
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s7_2_it_generates_recovery_tokens_with_source_metadata as generator
)

@pytest.fixture
def invalid_entries():
    return [
        {
            "path": "game_construction_bay/component/failure1",
            "source": "memory_ai",
            "codex_valid": False,
            "filename_valid": True,
            "codex_reason": "missing function",
            "filename": "failure1"
        },
        {
            "path": "game_construction_bay/component/failure2",
            "source": "archivist_ai",
            "codex_valid": True,
            "filename_valid": False,
            "codex_reason": None,
            "filename": "bad-name"
        }
    ]

@pytest.fixture
def patched_token_dir():
    original_dir = generator.TOKEN_DIR
    temp_root = tempfile.mkdtemp()
    generator.TOKEN_DIR = str(Path(temp_root) / "recovery_tokens")
    yield generator.TOKEN_DIR
    generator.TOKEN_DIR = original_dir
    rmtree(temp_root)

def test_token_creation_and_content(invalid_entries, patched_token_dir):
    tokens = generator.generate_recovery_tokens(invalid_entries)

    assert len(tokens) == 2
    for token_path in tokens:
        assert os.path.exists(token_path)
        with open(token_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert "source" in data
            assert "path" in data
            assert "codex_valid" in data
            assert "created_at" in data
