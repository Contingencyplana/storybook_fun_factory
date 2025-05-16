"""
Test: test_s4_3_it_resolves_pending_recursions_from_other_layers.py

Validates the behavior of resolve_pending_recursions_from_other_layers using 📜 5.5 dynamic import methodology.
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
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s4_3_it_resolves_pending_recursions_from_other_layers.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
resolve_pending_recursions_from_other_layers = module.resolve_pending_recursions_from_other_layers

def test_resolve_returns_valid_data(tmp_path):
    sample_data = [
        {"id": "R101", "status": "pending"},
        {"id": "R102", "status": "waiting"}
    ]

    pending_file = tmp_path / "pending_recursions.json"
    with pending_file.open("w", encoding="utf-8") as f:
        json.dump(sample_data, f)

    result = resolve_pending_recursions_from_other_layers(source_dir=tmp_path)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == "R101"

def test_resolve_raises_if_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        resolve_pending_recursions_from_other_layers(source_dir=tmp_path)
