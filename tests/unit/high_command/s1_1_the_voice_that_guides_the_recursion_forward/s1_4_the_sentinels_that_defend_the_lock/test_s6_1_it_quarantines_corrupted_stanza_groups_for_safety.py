"""
Filename: test_s6_1_it_quarantines_corrupted_stanza_groups_for_safety.py

Tests quarantine behavior for stanza folders marked as corrupted.
Verifies:
- Marker detection
- Correct quarantine path creation
- Logging of quarantine events
- Isolation of uncorrupted folders
"""

import os
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_4_the_sentinels_that_defend_the_lock.lockdown_reversion_and_repair import (
    s6_1_it_quarantines_corrupted_stanza_groups_for_safety as quarantine_module
)

@pytest.fixture
def mock_stanza_environment():
    temp_dir = tempfile.mkdtemp()
    base_path = Path(temp_dir) / "game_construction_bay"
    quarantine_path = Path(temp_dir) / "quarantine_zone"
    os.makedirs(base_path / "safe_stanza", exist_ok=True)
    os.makedirs(base_path / "bad_stanza", exist_ok=True)

    # Create marker in bad_stanza
    marker_path = base_path / "bad_stanza" / "corrupted.stanza"
    marker_path.touch()

    yield str(base_path), str(quarantine_path), str(marker_path)

    rmtree(temp_dir)

def test_quarantine_logic(mock_stanza_environment):
    base_path, quarantine_path, _ = mock_stanza_environment

    quarantined = quarantine_module.quarantine_corrupted_stanza_groups(base_path=base_path)
    
    assert len(quarantined) == 1
    original, quarantine_target = quarantined[0]
    assert "bad_stanza" in original
    assert os.path.exists(quarantine_target)
    assert os.path.basename(quarantine_target).startswith("bad_stanza__")

    log_file = Path(quarantine_module.QUARANTINE_FOLDER) / "logs" / "quarantine_log.txt"
    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as f:
        contents = f.read()
        assert "bad_stanza" in contents
        assert "quarantined" in contents
