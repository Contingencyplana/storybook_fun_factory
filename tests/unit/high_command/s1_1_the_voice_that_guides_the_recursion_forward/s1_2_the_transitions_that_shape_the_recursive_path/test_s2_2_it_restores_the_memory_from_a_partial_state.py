"""
Test for s2_2_it_restores_the_memory_from_a_partial_state.py
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
def snapshot_file(tmp_path):
    def _write_snapshot(content: dict):
        path = tmp_path / "snapshot.json"
        path.write_text(json.dumps(content), encoding="utf-8")
        return path
    return _write_snapshot


# ✅ Ensure this function is top-level and begins with `test_`
def test_restore_partial_memory(snapshot_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s2_2_it_restores_the_memory_from_a_partial_state.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Scenario 1: Valid memory
    log_file = snapshot_file({"memory_state": {"cycle": "filename_ai"}})
    assert module.restore_partial_memory(log_file) == {"cycle": "filename_ai"}

    # Scenario 2: Empty memory_state
    log_file = snapshot_file({"memory_state": {}})
    assert module.restore_partial_memory(log_file) == {}

    # Scenario 3: Missing memory_state
    log_file = snapshot_file({"other": 123})
    assert module.restore_partial_memory(log_file) == {}

    # Scenario 4: Corrupt JSON
    corrupt = log_file.parent / "corrupt.json"
    corrupt.write_text("{ not json ", encoding="utf-8")
    assert module.restore_partial_memory(corrupt) == {}

    # Scenario 5: Missing file
    missing = log_file.parent / "missing.json"
    assert module.restore_partial_memory(missing) == {}
