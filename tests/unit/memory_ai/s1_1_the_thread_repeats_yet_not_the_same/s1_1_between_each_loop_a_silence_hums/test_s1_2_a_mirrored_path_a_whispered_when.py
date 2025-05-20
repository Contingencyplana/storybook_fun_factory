"""
Filename: test_s1_2_a_mirrored_path_a_whispered_when.py

Tests s1_2_a_mirrored_path_a_whispered_when.py

Validates timestamp logging, retrieval, and time delta calculation
for temporal recursion-aware memory traces.
"""

import os
import sys
import json
import time
import pytest
import importlib.util
from pathlib import Path

# ✅ Ensure src/ is in sys.path
project_root = os.path.abspath(os.getcwd())
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# ✅ Load dynamic_importer
helper_path = os.path.join(project_root, "tests", "test_helpers", "dynamic_importer.py")
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the module under test
trace_module = dynamic_importer.dynamic_import_module(
    os.path.join(
        "src", "storybook_fun_factory", "memory_ai",
        "s1_1_the_thread_repeats_yet_not_the_same",
        "s1_1_between_each_loop_a_silence_hums",
        "s1_2_a_mirrored_path_a_whispered_when.py"
    )
)

@pytest.fixture
def temp_trace_env(tmp_path, monkeypatch):
    """Redirect trace log file to isolated temp folder."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "timestamp_traces.json"

    monkeypatch.setattr(trace_module, "TIME_TRACE_DIR", fake_dir)
    monkeypatch.setattr(trace_module, "TIME_TRACE_FILE", fake_file)

    yield fake_file

def test_store_and_load_new_event(temp_trace_env):
    event_key = "test_event_alpha"
    trace_module.store_timestamp_event(event_key)

    with open(temp_trace_env, "r") as f:
        data = json.load(f)

    assert event_key in data
    assert isinstance(data[event_key], list)
    assert len(data[event_key]) == 1

def test_time_since_last_event_first_call(temp_trace_env):
    event_key = "new_event_never_seen"
    elapsed = trace_module.time_since_last_event(event_key)
    assert elapsed == -1

def test_time_since_last_event_return_value(temp_trace_env):
    event_key = "timed_event"
    trace_module.store_timestamp_event(event_key)

    time.sleep(1)  # Introduce delay to measure

    elapsed = trace_module.time_since_last_event(event_key)
    assert elapsed >= 1
