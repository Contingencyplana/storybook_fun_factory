"""
Tests for _1_4_now_marks_the_path_the_mind_replayed.py

Validates memory replay behavior for previously stored recursion signatures.
"""

import json
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _1_4_now_marks_the_path_the_mind_replayed as replay_module

@pytest.fixture
def temp_replay_log(tmp_path, monkeypatch):
    """Redirect the replay trace file to an isolated environment."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "recursion_signatures.json"

    monkeypatch.setattr(replay_module, "REPLAY_LOG_DIR", fake_dir)
    monkeypatch.setattr(replay_module, "REPLAY_TRACE_FILE", fake_file)

    yield fake_file

def test_load_trace_sequence_empty(temp_replay_log):
    traces = replay_module.load_trace_sequence()
    assert traces == []

def test_load_trace_sequence_with_data(temp_replay_log):
    sample_data = [
        {"timestamp": "2025-04-19T10:00:00", "action": "begin"},
        {"timestamp": "2025-04-19T10:01:00", "action": "turn"}
    ]
    with open(temp_replay_log, "w") as f:
        json.dump(sample_data, f)

    traces = replay_module.load_trace_sequence()
    assert isinstance(traces, list)
    assert len(traces) == 2
    assert traces[0]["action"] == "begin"

def test_simulate_replay_sequential():
    traces = [
        {"timestamp": "T1", "action": "jump"},
        {"timestamp": "T2", "action": "loop"}
    ]
    result = replay_module.simulate_replay(traces, strategy="sequential")
    assert result[0] == "Replayed: jump @ T1"
    assert result[1] == "Replayed: loop @ T2"

def test_simulate_replay_reverse():
    traces = [
        {"timestamp": "T1", "action": "init"},
        {"timestamp": "T2", "action": "reflect"}
    ]
    result = replay_module.simulate_replay(traces, strategy="reverse")
    assert result[0] == "Echoed: reflect from T2"
    assert result[1] == "Echoed: init from T1"

def test_simulate_replay_unknown_strategy():
    traces = [{"timestamp": "T1", "action": "unknown"}]
    result = replay_module.simulate_replay(traces, strategy="zigzag")
    assert "(Unknown strategy" in result[0]

def test_simulate_replay_empty_input():
    result = replay_module.simulate_replay([], strategy="sequential")
    assert "(No past memory traces found.)" in result[0]
