"""
Filename: test_s2_1_a_breath_recalled_from_threads_once_spun.py

Tests s2_1_a_breath_recalled_from_threads_once_spun.py

Validates memory trace recall functionality with selective filters
based on component, action, and timestamp thresholds.
"""

import json
import pytest
from pathlib import Path
from datetime import datetime, timedelta

from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _2_1_a_breath_recalled_from_threads_once_spun as recall_module

@pytest.fixture
def temp_trace_log(tmp_path, monkeypatch):
    """Redirects memory trace path to a temporary file."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "recursion_signatures.json"

    monkeypatch.setattr(recall_module, "TRACE_DIR", fake_dir)
    monkeypatch.setattr(recall_module, "TRACE_FILE", fake_file)

    return fake_file

def test_load_memory_traces_empty(temp_trace_log):
    traces = recall_module.load_memory_traces()
    assert traces == []

def test_load_memory_traces_with_data(temp_trace_log):
    data = [
        {"component": "memory_ai", "action": "start", "timestamp": "2025-04-19T00:00:00"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    traces = recall_module.load_memory_traces()
    assert isinstance(traces, list)
    assert traces[0]["action"] == "start"

def test_filter_by_component(temp_trace_log):
    data = [
        {"component": "memory_ai", "action": "start", "timestamp": "2025-04-19T00:00:00"},
        {"component": "dream_journal", "action": "reflect", "timestamp": "2025-04-19T01:00:00"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    filtered = recall_module.filter_traces(component="memory_ai")
    assert len(filtered) == 1
    assert filtered[0]["component"] == "memory_ai"

def test_filter_by_action(temp_trace_log):
    data = [
        {"component": "memory_ai", "action": "start", "timestamp": "2025-04-19T00:00:00"},
        {"component": "memory_ai", "action": "loop", "timestamp": "2025-04-19T01:00:00"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    filtered = recall_module.filter_traces(action="loop")
    assert len(filtered) == 1
    assert filtered[0]["action"] == "loop"

def test_filter_by_timestamp(temp_trace_log):
    now = datetime.now()
    before = now - timedelta(days=2)
    after = now + timedelta(days=1)

    data = [
        {"component": "memory_ai", "action": "early", "timestamp": before.isoformat()},
        {"component": "memory_ai", "action": "future", "timestamp": after.isoformat()}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    filtered = recall_module.filter_traces(since=now.isoformat())
    assert len(filtered) == 1
    assert filtered[0]["action"] == "future"
