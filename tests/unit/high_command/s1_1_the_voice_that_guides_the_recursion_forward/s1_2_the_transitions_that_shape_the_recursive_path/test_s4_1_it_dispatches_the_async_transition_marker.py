"""
Test: test_s4_1_it_dispatches_the_async_transition_marker.py

Validates the behavior of dispatch_async_transition_marker using 📜 5.5 dynamic import methodology.
"""

import os
import json
import importlib.util
from pathlib import Path

import pytest

# Load dynamic_importer helper
HELPER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the module under test
MODULE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../game_construction_bay/high_command/s1_2_the_transitions_that_shape_the_recursive_path/s4_1_it_dispatches_the_async_transition_marker.py")
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
dispatch_async_transition_marker = module.dispatch_async_transition_marker

def test_dispatch_async_transition_marker_creates_marker(tmp_path):
    metadata = {
        "transition_id": "T123",
        "stanza": "s4_1",
        "note": "Test async dispatch"
    }

    marker_path = dispatch_async_transition_marker(
        destination="memory_ai", metadata=metadata, output_dir=tmp_path
    )

    assert marker_path.exists()
    with marker_path.open("r", encoding="utf-8") as f:
        marker_data = json.load(f)

    assert marker_data["destination"] == "memory_ai"
    assert marker_data["metadata"]["transition_id"] == "T123"
    assert "dispatched_at" in marker_data
