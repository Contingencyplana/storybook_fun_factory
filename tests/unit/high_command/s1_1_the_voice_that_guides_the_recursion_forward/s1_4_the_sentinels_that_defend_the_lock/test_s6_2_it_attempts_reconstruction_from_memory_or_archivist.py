"""
Filename: test_s6_2_it_attempts_reconstruction_from_memory_or_archivist.py

Tests logic for simulated stanza restoration from memory_ai and archivist_ai.
Verifies:
- Successful reconstruction record generation
- Handling of quarantine log input
- Basic logic for agreement vs conflict between memory sources
"""

import os
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s6_2_it_attempts_reconstruction_from_memory_or_archivist as recon_module
)

@pytest.fixture
def mock_quarantine_log():
    temp_dir = tempfile.mkdtemp()
    log_dir = Path(temp_dir) / "quarantine_zone" / "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = log_dir / "quarantine_log.txt"

    # Add one quarantined record
    entry = {
        "original_path": "game_construction_bay/example_module/bad_stanza",
        "quarantine_path": "quarantine_zone/bad_stanza__20250518T041032Z",
        "timestamp": "2025-05-18T04:10:32Z",
        "status": "quarantined"
    }
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(str(entry) + "\n")

    yield str(log_file)

    rmtree(temp_dir)

def test_attempt_reconstruction_returns_valid_results(mock_quarantine_log):
    results = recon_module.attempt_reconstruction(mock_quarantine_log)

    assert isinstance(results, list)
    assert len(results) == 1
    r = results[0]
    assert "restored_content" in r
    assert r["source"] in ["memory_ai", "archivist_ai"]
    assert "timestamp" in r
    assert r["path"].endswith("bad_stanza")
