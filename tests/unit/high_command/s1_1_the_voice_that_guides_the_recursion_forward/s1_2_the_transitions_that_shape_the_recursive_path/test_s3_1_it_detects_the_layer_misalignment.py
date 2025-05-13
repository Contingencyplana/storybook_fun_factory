"""
Test for s3_1_it_detects_the_layer_misalignment.py
Uses 📜 5.5-compliant dynamic import methodology.
"""

import os
import json
import importlib.util
from pathlib import Path
import pytest


def dynamic_import_module(module_path: str, module_name: str = "dynamic_module"):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def metadata_file(tmp_path):
    def _write_metadata(source_layer, target_layer):
        metadata_path = tmp_path / "transition_metadata.json"
        metadata = {"source_layer": source_layer, "target_layer": target_layer}
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        return metadata_path
    return _write_metadata


def test_layer_misalignment_detection(metadata_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_2_the_transitions_that_shape_the_recursive_path/cycle_2_asynchronous_crosslayer_recursion/s3_1_it_detects_the_layer_misalignment.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Valid transition
    valid = metadata_file("layer_1", "layer_2")
    assert module.detect_layer_misalignment(valid) is False

    # Invalid transition
    invalid = metadata_file("layer_1", "layer_3")
    assert module.detect_layer_misalignment(invalid) is True

    # Unknown source
    unknown = metadata_file("unknown_layer", "layer_2")
    assert module.detect_layer_misalignment(unknown) is True

    # Missing layer connection
    broken = metadata_file("layer_2", "layer_99")
    assert module.detect_layer_misalignment(broken) is True
