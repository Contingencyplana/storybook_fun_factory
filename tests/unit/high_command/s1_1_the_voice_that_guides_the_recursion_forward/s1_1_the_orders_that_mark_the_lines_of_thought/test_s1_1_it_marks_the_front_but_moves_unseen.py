"""
Test File: test_1_1_it_marks_the_front_but_moves_unseen.py

📜 Tests the Genesis Command logic in:
s1_1_it_marks_the_front_but_moves_unseen.py

Validates that High Command can:
• Mark the current active recursive front
• Retrieve and print it correctly
• Store and overwrite the active_front.json file cleanly
"""

import os
import json
import shutil
import tempfile
from pathlib import Path

import pytest

# ✅ Import the module under test
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_1_it_marks_the_front_but_moves_unseen as genesis_cmd
)

@pytest.fixture
def temp_front_path(monkeypatch):
    """
    Fixture to isolate the ACTIVE_FRONT_PATH to a temporary directory.
    """
    temp_dir = Path(tempfile.mkdtemp())
    fake_path = temp_dir / "active_front.json"
    monkeypatch.setattr(genesis_cmd, "ACTIVE_FRONT_PATH", fake_path)
    yield fake_path
    shutil.rmtree(temp_dir)

def test_mark_and_get_active_front(temp_front_path):
    """
    Ensure that marking and retrieving the active front works correctly.
    """
    test_data = {
        "component_name": "visualizer",
        "stanza_id": "s3_2_the_map_that_knows_the_flame",
        "line_filename": "_2_3_loops_do_not_always_close.py",
        "gdj_reference": "📜 4.74"
    }

    # Mark the front
    genesis_cmd.mark_active_front(
        component_name=test_data["component_name"],
        stanza_id=test_data["stanza_id"],
        line_filename=test_data["line_filename"],
        gdj_reference=test_data["gdj_reference"]
    )

    # Read it back
    result = genesis_cmd.get_active_front()

    assert result["component"] == test_data["component_name"]
    assert result["stanza"] == test_data["stanza_id"]
    assert result["line"] == test_data["line_filename"]
    assert result["gdj"] == test_data["gdj_reference"]

def test_get_active_front_returns_empty_when_missing(monkeypatch):
    """
    Ensure that get_active_front returns an empty dict when the file doesn't exist.
    """
    fake_path = Path(tempfile.mkdtemp()) / "nonexistent_front.json"
    monkeypatch.setattr(genesis_cmd, "ACTIVE_FRONT_PATH", fake_path)
    result = genesis_cmd.get_active_front()
    assert result == {}
