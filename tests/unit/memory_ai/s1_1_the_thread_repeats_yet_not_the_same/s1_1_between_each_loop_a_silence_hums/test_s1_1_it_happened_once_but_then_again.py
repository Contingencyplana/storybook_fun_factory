"""
Filename: test_s1_1_it_happened_once_but_then_again.py

Tests s1_1_it_happened_once_but_then_again.py

Uses Dynamic Import Methodology (📜 5.5: May 3, 4:05 – Canonizing the Dynamic Import Test Methodology)

Validates the ability to detect recursive signature loops based on
context hashing and log storage.
"""

import os
import sys
import importlib.util
import json
import pytest
from pathlib import Path

# ✅ CRITICAL: Ensure src/ is in sys.path *before* dynamic_importer or stanza are loaded
project_root = os.path.abspath(os.getcwd())
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Load dynamic_importer after sys.path is correctly configured
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza module under test
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        src_path,
        "storybook_fun_factory",
        "memory_ai",
        "s1_1_the_thread_repeats_yet_not_the_same",
        "s1_1_between_each_loop_a_silence_hums",
        "s1_1_it_happened_once_but_then_again.py",
    )
)

# Access the target function
detect_recursion_signature = module.detect_recursion_signature

@pytest.fixture
def temp_memory_log(tmp_path, monkeypatch):
    """Temporarily redirect memory log path to an isolated test directory."""
    test_log_dir = tmp_path / "storybook_fun_factory" / "memory_ai" / "memory_chain" / "trace_logs"
    test_log_dir.mkdir(parents=True, exist_ok=True)
    test_log_file = test_log_dir / "recursion_signatures.json"

    monkeypatch.setattr(module, "MEMORY_LOG_DIR", test_log_dir)
    monkeypatch.setattr(module, "MEMORY_LOG_FILE", test_log_file)

    yield test_log_file

def test_new_context_detected_as_new(temp_memory_log):
    context = {
        "timestamp": "2025-04-19T11:00:00",
        "component": "memory_ai",
        "action": "test_case",
        "stanza": "test_one"
    }

    result = detect_recursion_signature(context)
    assert result is False

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

    # First time: should store it
    assert detect_recursion_signature(context) is False

    # Second time: should detect it
    assert detect_recursion_signature(context) is True
