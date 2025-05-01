"""
Filename: test_s1_1_it_happened_once_but_then_again.py

Tests _s1_1_it_happened_once_but_then_again.py

Validates the ability to detect recursive signature loops based on
context hashing and log storage.
"""

import os
import json
import shutil
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _1_1_it_happened_once_but_then_again as recursion_module

@pytest.fixture
def temp_memory_log(tmp_path, monkeypatch):
    """Temporarily redirect the memory log path to an isolated test directory."""
    test_log_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    test_log_dir.mkdir(parents=True, exist_ok=True)
    test_log_file = test_log_dir / "recursion_signatures.json"

    monkeypatch.setattr(recursion_module, "MEMORY_LOG_DIR", test_log_dir)
    monkeypatch.setattr(recursion_module, "MEMORY_LOG_FILE", test_log_file)

    yield test_log_file

    # Cleanup handled by tmp_path fixture

def test_new_context_detected_as_new(temp_memory_log):
    context = {
        "timestamp": "2025-04-19T11:00:00",
        "component": "memory_ai",
        "action": "test_case",
        "stanza": "test_one"
    }

    result = recursion_module.detect_recursion_signature(context)
    assert result is False

    # Ensure the hash was stored
    with open(temp_memory_log, "r") as f:
        stored = json.load(f)
    assert isinstance(stored, list)
    assert len(stored) == 1

def test_repeat_context_detected_as_recursion(temp_memory_log):
    context = {
        "timestamp": "2025-04-19T11:00:00",
        "component": "memory_ai",
        "action": "test_case",
        "stanza": "test_one"
    }

    # First time: store it
    first = recursion_module.detect_recursion_signature(context)
    assert first is False

    # Second time: detect recursion
    second = recursion_module.detect_recursion_signature(context)
    assert second is True
