"""
Filename: test_s1_3_the_thread_that_bent_the_test_that_stayed.py

Tests _s1_3_the_thread_that_bent_the_test_that_stayed.py

Verifies detection and storage of branching points in recursive memory.
"""

import json
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _1_3_the_thread_that_bent_the_test_that_stayed as branch_module

@pytest.fixture
def temp_branch_log(tmp_path, monkeypatch):
    """Redirect the deviation log file to a temporary directory."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "branching_points.json"

    monkeypatch.setattr(branch_module, "DEVIATION_LOG_DIR", fake_dir)
    monkeypatch.setattr(branch_module, "DEVIATION_LOG_FILE", fake_file)

    yield fake_file

def test_records_new_branch(temp_branch_log):
    path = ["A", "B", "C"]
    result = "fork_one"

    msg = branch_module.record_branch_point(path, result)
    assert msg.startswith("🌱 New branch recorded")

    with open(temp_branch_log, "r") as f:
        data = json.load(f)

    assert isinstance(data, dict)
    assert len(data) == 1

def test_detects_existing_branch(temp_branch_log):
    path = ["X", "Y", "Z"]
    result = "loop_result"

    # First record should create the branch
    first = branch_module.record_branch_point(path, result)
    assert first.startswith("🌱 New branch")

    # Second should recognize it
    second = branch_module.record_branch_point(path, result)
    assert second.startswith("↩️ Branch previously recorded")

def test_branch_hash_consistency():
    path1 = ["alpha", "beta", "gamma"]
    path2 = ["alpha", "beta", "gamma"]

    hash1 = branch_module.hash_decision_path(path1)
    hash2 = branch_module.hash_decision_path(path2)

    assert hash1 == hash2
