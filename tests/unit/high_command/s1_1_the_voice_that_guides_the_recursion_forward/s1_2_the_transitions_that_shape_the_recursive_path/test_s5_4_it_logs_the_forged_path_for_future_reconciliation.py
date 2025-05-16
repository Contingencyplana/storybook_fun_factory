"""
Test: test_s5_4_it_logs_the_forged_path_for_future_reconciliation.py

Validates the logging of forged recursion paths using 📜 5.5 dynamic import methodology.
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
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s5_4_it_logs_the_forged_path_for_future_reconciliation.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
log_forged_path = module.log_forged_path

def test_log_forged_path_creates_log_entry(tmp_path):
    metadata = {
        "trace_id": "XYZ123",
        "system": "dream_journal",
        "anomaly": "checksum mismatch"
    }

    log_path = log_forged_path(
        origin="filename_ai",
        reason="Signature mismatch",
        metadata=metadata,
        output_dir=tmp_path
    )

    assert log_path.exists()

    with log_path.open("r", encoding="utf-8") as f:
        log_data = json.load(f)

    assert isinstance(log_data, list)
    assert len(log_data) == 1
    assert log_data[0]["origin"] == "filename_ai"
    assert log_data[0]["reason"] == "Signature mismatch"
    assert log_data[0]["metadata"]["trace_id"] == "XYZ123"

def test_log_forged_path_appends_to_existing_log(tmp_path):
    existing_log = [
        {"timestamp": "2025-05-16T12:00:00", "origin": "memory_ai", "reason": "Drift", "metadata": {}}
    ]
    log_path = tmp_path / "forged_recursion_log.json"
    with log_path.open("w", encoding="utf-8") as f:
        json.dump(existing_log, f, indent=2)

    new_metadata = {"trace_id": "ABC999", "system": "visualizer", "anomaly": "tamper detected"}
    result_path = log_forged_path(
        origin="visualizer",
        reason="Trace override detected",
        metadata=new_metadata,
        output_dir=tmp_path
    )

    assert result_path.exists()
    with result_path.open("r", encoding="utf-8") as f:
        new_log_data = json.load(f)

    assert len(new_log_data) == 2
    assert new_log_data[1]["metadata"]["system"] == "visualizer"
