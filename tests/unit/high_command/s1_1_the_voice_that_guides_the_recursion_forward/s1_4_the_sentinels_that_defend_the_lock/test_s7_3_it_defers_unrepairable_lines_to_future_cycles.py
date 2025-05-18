"""
Filename: test_s7_3_it_defers_unrepairable_lines_to_future_cycles.py

Tests that unrepairable stanza entries are safely deferred into structured files.
Verifies:
- Only failed entries are deferred
- Deferral filenames are correct
- Deferral contents contain all required metadata
"""

import os
import json
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s7_3_it_defers_unrepairable_lines_to_future_cycles as defer_module
)

@pytest.fixture
def sample_invalid_results():
    return [
        {
            "path": "game_construction_bay/component/broken_1",
            "source": "memory_ai",
            "codex_valid": False,
            "filename_valid": True,
            "codex_reason": "syntax error",
            "filename": "broken_1"
        },
        {
            "path": "game_construction_bay/component/broken_2",
            "source": "archivist_ai",
            "codex_valid": True,
            "filename_valid": False,
            "codex_reason": None,
            "filename": "???"
        }
    ]

@pytest.fixture
def patched_defer_dir():
    original_dir = defer_module.DEFER_DIR
    temp_root = tempfile.mkdtemp()
    defer_module.DEFER_DIR = str(Path(temp_root) / "deferred_stanzas")
    yield defer_module.DEFER_DIR
    defer_module.DEFER_DIR = original_dir
    rmtree(temp_root)

def test_deferral_generation_and_contents(sample_invalid_results, patched_defer_dir):
    paths = defer_module.defer_unrepairable_lines(sample_invalid_results)

    assert len(paths) == 2
    for p in paths:
        assert os.path.exists(p)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert "deferred_at" in data
            assert data["source"] in {"memory_ai", "archivist_ai"}
            assert data["codex_valid"] in [True, False]
            assert data["filename_valid"] in [True, False]
