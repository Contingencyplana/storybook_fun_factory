"""
Test File: test_s2_1_when_a_component_falls_another_rises.py

📜 Tests the component pivot logic in:
s2_1_when_a_component_falls_another_rises.py

Ensures the system can detect stagnation and recommend a new component.
"""

import json
import shutil
import tempfile
from datetime import datetime, timedelta, UTC
from pathlib import Path

import pytest

from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s2_1_when_a_component_falls_another_rises as pivot
)

@pytest.fixture
def temp_state(monkeypatch):
    """
    Fixture to redirect active_front.json and stanza_path_log.json to temp files.
    """
    temp_dir = Path(tempfile.mkdtemp())
    front_path = temp_dir / "active_front.json"
    trace_path = temp_dir / "stanza_path_log.json"

    # Inject monkeypatched paths
    monkeypatch.setattr(pivot, "ACTIVE_FRONT_PATH", front_path)
    monkeypatch.setattr(pivot, "STANZA_TRACE_PATH", trace_path)

    yield front_path, trace_path
    shutil.rmtree(temp_dir)

def test_no_data_when_files_missing(temp_state):
    """
    Should return 'no_data' when trace file is missing or empty.
    """
    front_path, trace_path = temp_state
    result = pivot.detect_and_pivot_if_stalled()
    assert result["status"] == "no_data"

def test_pivot_when_timeout_exceeded(temp_state):
    """
    Simulates a trace log with a very old
