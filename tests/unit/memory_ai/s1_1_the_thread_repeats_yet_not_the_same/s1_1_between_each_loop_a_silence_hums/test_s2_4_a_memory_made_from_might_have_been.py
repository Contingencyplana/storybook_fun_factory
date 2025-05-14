"""
Filename: test_s2_4_a_memory_made_from_might_have_been.py

Tests s2_4_a_memory_made_from_might_have_been.py

Validates generation of counterfactual memory variants from past traces.
"""

import json
import pytest
from pathlib import Path
from storybook_fun_factory.memory_ai._1_1_the_thread_repeats_yet_not_the_same._1_1_between_each_loop_a_silence_hums import _2_4_a_memory_made_from_might_have_been as cf_module

@pytest.fixture
def temp_trace_log(tmp_path, monkeypatch):
    """Redirects memory trace path to a temporary location."""
    fake_dir = tmp_path / "memory_ai" / "memory_chain" / "trace_logs"
    fake_dir.mkdir(parents=True, exist_ok=True)
    fake_file = fake_dir / "recursion_signatures.json"

    monkeypatch.setattr(cf_module, "TRACE_DIR", fake_dir)
    monkeypatch.setattr(cf_module, "TRACE_FILE", fake_file)

    return fake_file

def test_load_traces_empty(temp_trace_log):
    traces = cf_module.load_traces()
    assert traces == []

def test_generate_counterfactual_structure(temp_trace_log):
    original = [
        {"component": "memory_ai", "action": "observe", "timestamp": "2025-04-19T00:00:00"},
        {"component": "dream_journal", "action": "reflect", "timestamp": "2025-04-19T01:00:00"}
    ]
    with open(temp_trace_log, "w") as f:
        json.dump(original, f)

    traces = cf_module.load_traces()
    variants = cf_module.generate_counterfactual_variants(traces, max_variants=2)

    assert len(variants) <= 2
    for v in variants:
        assert v.get("counterfactual") is True
        assert "original_hash" in v
        assert v.get("action") in ["invert", "skip", "repeat", "redirect", "branch"]
        assert v.get("component") in ["memory_ai", "filename_ai", "dream_journal"]
        assert v.get("note") == "Simulated alternative outcome"

def test_generate_counterfactual_max_limit(temp_trace_log):
    data = [{"component": "memory_ai", "action": f"act{i}", "timestamp": f"2025-04-19T{i:02}:00:00"} for i in range(10)]
    with open(temp_trace_log, "w") as f:
        json.dump(data, f)

    traces = cf_module.load_traces()
    variants = cf_module.generate_counterfactual_variants(traces, max_variants=3)

    assert len(variants) == 3
