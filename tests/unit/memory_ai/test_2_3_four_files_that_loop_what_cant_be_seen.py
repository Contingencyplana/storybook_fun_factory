"""
Tests for _2_3_four_files_that_loop_what_cant_be_seen.py

Validates loop detection logic by simulating trace signatures
and identifying recurring memory event patterns.
"""

import json
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _2_3_four_files_that_loop_what_cant_be_seen as loop_module

@pytest.fixture
def temp_trace_log(tmp_path, monkeypatch):
    """Redirects memory trace path to a temporary file."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "recursion_signatures.json"

    monkeypatch.setattr(loop_module, "TRACE_DIR", fake_dir)
    monkeypatch.setattr(loop_module, "TRACE_FILE", fake_file)

    return fake_file

def test_load_all_traces_empty(temp_trace_log):
    traces = loop_module.load_all_traces()
    assert traces == []

def test_generate_trace_signature_consistency():
    trace1 = {"component": "memory_ai", "action": "reflect"}
    trace2 = {"component": "memory_ai", "action": "reflect"}

    sig1 = loop_module.generate_trace_signature(trace1)
    sig2 = loop_module.generate_trace_signature(trace2)

    assert sig1 == sig2
    assert isinstance(sig1, str)
    assert len(sig1) == 64  # SHA-256 hash length

def test_detect_loop_clusters_none(temp_trace_log):
    unique_traces = [
        {"component": "filename_ai", "action": "generate"},
        {"component": "memory_ai", "action": "observe"},
        {"component": "dream_journal", "action": "transform"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(unique_traces, f)

    loops = loop_module.detect_loop_clusters()
    assert loops == {}

def test_detect_loop_clusters_some(temp_trace_log):
    repeating_traces = [
        {"component": "memory_ai", "action": "loop"},
        {"component": "memory_ai", "action": "loop"},
        {"component": "memory_ai", "action": "loop"},
        {"component": "filename_ai", "action": "build"},
        {"component": "filename_ai", "action": "build"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(repeating_traces, f)

    loops = loop_module.detect_loop_clusters()
    assert isinstance(loops, dict)
    assert all(count > 1 for count in loops.values())
    assert len(loops) == 2
