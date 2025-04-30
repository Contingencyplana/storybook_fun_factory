"""
Tests for _2_2_a_choice_rebuilt_from_what_was_done.py

Validates reconstruction of past decision chains from stored memory traces.
"""

import json
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _2_2_a_choice_rebuilt_from_what_was_done as choice_module

@pytest.fixture
def temp_trace_log(tmp_path, monkeypatch):
    """Redirects memory trace path to a temporary log file."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "recursion_signatures.json"

    monkeypatch.setattr(choice_module, "TRACE_DIR", fake_dir)
    monkeypatch.setattr(choice_module, "TRACE_FILE", fake_file)

    return fake_file

def test_load_past_choices_empty(temp_trace_log):
    choices = choice_module.load_past_choices()
    assert choices == []

def test_reconstruct_exact_match(temp_trace_log):
    data = [
        {"action": "observe"},
        {"action": "reflect"},
        {"action": "choose"},
        {"action": "ignore"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    pattern = ["observe", "reflect", "choose"]
    results = choice_module.reconstruct_choices_by_action_chain(pattern)

    assert len(results) == 1
    assert [step["action"] for step in results[0]] == pattern

def test_reconstruct_with_intervening_action_and_tolerance(temp_trace_log):
    data = [
        {"action": "observe"},
        {"action": "wait"},
        {"action": "reflect"},
        {"action": "choose"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    pattern = ["observe", "reflect", "choose"]
    results = choice_module.reconstruct_choices_by_action_chain(pattern, tolerance=1)

    assert len(results) == 1
    assert "reflect" in [step["action"] for step in results[0]]

def test_reconstruct_with_insufficient_tolerance(temp_trace_log):
    data = [
        {"action": "observe"},
        {"action": "wait"},
        {"action": "reflect"},
        {"action": "choose"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    pattern = ["observe", "reflect", "choose"]
    results = choice_module.reconstruct_choices_by_action_chain(pattern, tolerance=0)

    assert len(results) == 0

def test_reconstruct_multiple_chains(temp_trace_log):
    data = [
        {"action": "observe"},
        {"action": "reflect"},
        {"action": "choose"},
        {"action": "observe"},
        {"action": "reflect"},
        {"action": "choose"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    pattern = ["observe", "reflect", "choose"]
    results = choice_module.reconstruct_choices_by_action_chain(pattern)

    assert len(results) == 2
