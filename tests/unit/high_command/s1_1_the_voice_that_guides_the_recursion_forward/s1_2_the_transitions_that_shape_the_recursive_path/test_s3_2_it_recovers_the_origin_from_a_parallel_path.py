"""
Test for s3_2_it_recovers_the_origin_from_a_parallel_path.py
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
    def _write_metadata(current_position, recovery_map):
        metadata_path = tmp_path / "parallel_metadata.json"
        metadata = {
            "current_position": current_position,
            "recovery_map": recovery_map
        }
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        return metadata_path
    return _write_metadata


def test_origin_recovery(metadata_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s3_2_it_recovers_the_origin_from_a_parallel_path.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Recoverable case
    recoverable = metadata_file("ghost_layer", {"ghost_layer": "layer_2:start_sequence"})
    assert module.recover_origin_from_parallel_path(recoverable) == "layer_2:start_sequence"

    # Unrecoverable case
    unrecoverable = metadata_file("phantom_hole", {"ghost_layer": "layer_2:start_sequence"})
    assert module.recover_origin_from_parallel_path(unrecoverable) == "unknown_origin"
