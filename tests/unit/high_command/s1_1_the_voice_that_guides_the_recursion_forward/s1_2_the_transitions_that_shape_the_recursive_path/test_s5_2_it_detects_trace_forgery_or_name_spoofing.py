"""
Test: test_s5_2_it_detects_trace_forgery_or_name_spoofing.py

Validates is_trace_forged and compute_origin_hash using 📜 5.5 dynamic import protocol.
"""

import os
import json
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer helper
HELPER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the module under test
MODULE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s5_2_it_detects_trace_forgery_or_name_spoofing.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
is_trace_forged = module.is_trace_forged
compute_origin_hash = module.compute_origin_hash

def test_valid_trace(tmp_path):
    stanza_id = "S5.2"
    author = "trusted_user"
    timestamp = "2025-05-16T15:00:00Z"

    expected_hash = compute_origin_hash(stanza_id, author, timestamp)

    trace_data = {"origin_hash": expected_hash}
    trace_path = tmp_path / "stanza_trace.json"
    with trace_path.open("w", encoding="utf-8") as f:
        json.dump(trace_data, f)

    assert is_trace_forged(trace_path, expected_hash) is False

def test_forged_trace(tmp_path):
    trace_data = {"origin_hash": "invalid_fake_hash"}
    trace_path = tmp_path / "stanza_trace.json"
    with trace_path.open("w", encoding="utf-8") as f:
        json.dump(trace_data, f)

    assert is_trace_forged(trace_path, "expected_real_hash") is True
