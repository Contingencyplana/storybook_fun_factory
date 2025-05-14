"""
Test File: test_s1_3_it_traces_the_path_in_stanza_form.py

📜 Tests stanza path logging in:
s1_3_it_traces_the_path_in_stanza_form.py

Validates that stanza traversal history:
• Records properly
• Stores multiple entries
• Retrieves a bounded, most-recent slice
"""

import json
import shutil
import tempfile
from pathlib import Path

import pytest

# ✅ Import the module under test
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_3_it_traces_the_path_in_stanza_form as tracer
)

@pytest.fixture
def temp_trace_path(monkeypatch):
    """
    Fixture to isolate STANZA_TRACE_PATH to a temporary file.
    """
    temp_dir = Path(tempfile.mkdtemp())
    fake_path = temp_dir / "stanza_path_log.json"
    monkeypatch.setattr(tracer, "STANZA_TRACE_PATH", fake_path)
    yield fake_path
    shutil.rmtree(temp_dir)

def test_trace_and_retrieve_stanza_path(temp_trace_path):
    """
    Ensures trace entries are written and read back correctly.
    """
    # Add multiple entries
    for i in range(6):
        tracer.trace_stanza_progress(
            component="memory_ai",
            stanza=f"s{i}_example_stanza",
            line=f"_1_{i}_example_line.py"
        )

    traces = tracer.get_recent_traces(limit=3)

    assert len(traces) == 3
    assert traces[-1]["stanza"] == "s5_example_stanza"
    assert traces[-1]["line"] == "_1_5_example_line.py"

def test_trace_file_missing_returns_empty(temp_trace_path):
    """
    Ensures get_recent_traces returns empty list when no file exists.
    """
    if temp_trace_path.exists():
        temp_trace_path.unlink()
    traces = tracer.get_recent_traces()
    assert traces == []
