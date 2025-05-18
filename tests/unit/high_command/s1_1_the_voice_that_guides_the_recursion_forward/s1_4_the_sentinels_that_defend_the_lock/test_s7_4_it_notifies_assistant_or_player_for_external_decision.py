"""
Filename: test_s7_4_it_notifies_assistant_or_player_for_external_decision.py

Tests assistant/player notification system for unrecoverable stanza deferrals.
Verifies:
- Proper parsing of deferred .json entries
- Logging of external review needs
- Summary list generation
"""

import os
import json
import tempfile
from pathlib import Path
from shutil import rmtree

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s7_4_it_notifies_assistant_or_player_for_external_decision as notifier
)

@pytest.fixture
def mock_deferred_zone():
    temp_dir = tempfile.mkdtemp()
    deferred = Path(temp_dir) / "quarantine_zone" / "deferred"
    logs = deferred / "logs"
    os.makedirs(deferred, exist_ok=True)

    # Create a sample deferral entry
    sample_entry = {
        "path": "/mock/component_xyz",
        "source": "archivist_ai",
        "reason": "ambiguous codex trace"
    }
    entry_path = deferred / "component_xyz.json"
    with open(entry_path, "w", encoding="utf-8") as f:
        json.dump(sample_entry, f)

    yield str(deferred)

    rmtree(temp_dir)

def test_notify_external_review(mock_deferred_zone):
    result = notifier.notify_external_review(mock_deferred_zone)
    assert len(result) == 1
    assert "Awaiting review" in result[0]
    assert "component_xyz" in result[0]

    log_file = Path(mock_deferred_zone) / "logs" / "review_log.txt"
    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "component_xyz" in content
        assert "awaiting_review" in content
