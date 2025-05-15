"""
Test: test_s4_2_it_listens_for_crossphase_return_signals.py

Validates the behavior of listen_for_crossphase_return_signal using 📜 5.5 dynamic import methodology.
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
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s4_2_it_listens_for_crossphase_return_signals.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
listen_for_crossphase_return_signal = module.listen_for_crossphase_return_signal

def test_listen_for_crossphase_return_signal_reads_marker(tmp_path):
    expected_data = {
        "destination": "dream_journal",
        "metadata": {
            "transition_id": "T456",
            "stanza": "s4_2",
            "note": "Async signal reception test"
        },
        "dispatched_at": "2025-05-15T00:00:00Z"
    }

    marker_path = tmp_path / "async_transition_marker.json"
    with marker_path.open("w", encoding="utf-8") as f:
        json.dump(expected_data, f)

    result = listen_for_crossphase_return_signal(search_dir=tmp_path)

    assert result["destination"] == "dream_journal"
    assert result["metadata"]["transition_id"] == "T456"
    assert "dispatched_at" in result

def test_listen_for_crossphase_return_signal_raises_if_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        listen_for_crossphase_return_signal(search_dir=tmp_path)
