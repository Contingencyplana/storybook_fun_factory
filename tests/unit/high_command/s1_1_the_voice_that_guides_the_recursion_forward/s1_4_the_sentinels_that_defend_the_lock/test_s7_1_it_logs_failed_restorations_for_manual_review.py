"""
Filename: test_s7_1_it_logs_failed_restorations_for_manual_review.py

Tests the logging of invalid stanza restoration results for manual review.
Verifies:
- Only invalid entries are logged
- The failure log file is written correctly
- No logs are created for fully valid entries
"""

import os
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s7_1_it_logs_failed_restorations_for_manual_review as logger
)

@pytest.fixture
def sample_validated_entries():
    return [
        {
            "path": "game_construction_bay/component/valid_name",
            "source": "memory_ai",
            "codex_valid": True,
            "filename_valid": True,
            "codex_reason": None,
            "filename": "valid_name"
        },
        {
            "path": "game_construction_bay/component/broken",
            "source": "archivist_ai",
            "codex_valid": False,
            "filename_valid": True,
            "codex_reason": "forbidden syntax",
            "filename": "broken"
        },
        {
            "path": "game_construction_bay/component/ugly",
            "source": "memory_ai",
            "codex_valid": True,
            "filename_valid": False,
            "codex_reason": None,
            "filename": "bad_format"
        }
    ]

@pytest.fixture
def temp_failure_dir():
    original_dir = logger.FAILED_LOG_DIR
    original_file = logger.FAILED_LOG_FILE

    temp_root = tempfile.mkdtemp()
    logger.FAILED_LOG_DIR = str(Path(temp_root) / "failed_restorations")
    logger.FAILED_LOG_FILE = str(Path(logger.FAILED_LOG_DIR) / "failed_log.txt")

    yield logger.FAILED_LOG_FILE

    logger.FAILED_LOG_DIR = original_dir
    logger.FAILED_LOG_FILE = original_file
    rmtree(temp_root)

def test_log_failed_stanzas_creates_log(temp_failure_dir, sample_validated_entries):
    result = logger.log_failed_stanzas(sample_validated_entries)

    assert os.path.exists(result[0])
    with open(result[0], "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert "broken" in lines[0]
        assert "bad_format" in lines[1]

def test_no_log_created_for_valid_entries_only(temp_failure_dir):
    result = logger.log_failed_stanzas([
        {
            "path": "game_construction_bay/component/valid",
            "source": "memory_ai",
            "codex_valid": True,
            "filename_valid": True,
            "codex_reason": None,
            "filename": "valid"
        }
    ])

    assert result == []
    assert not os.path.exists(temp_failure_dir)
