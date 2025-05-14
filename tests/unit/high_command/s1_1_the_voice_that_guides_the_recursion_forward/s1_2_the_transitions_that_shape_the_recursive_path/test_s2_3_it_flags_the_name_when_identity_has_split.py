"""
Test for s2_3_it_flags_the_name_when_identity_has_split.py
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
def name_trace_file(tmp_path):
    def _write_trace(content: dict):
        path = tmp_path / "name_trace.json"
        path.write_text(json.dumps(content), encoding="utf-8")
        return path
    return _write_trace


def test_flag_identity_drift(name_trace_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s2_3_it_flags_the_name_when_identity_has_split.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Case 1: expected != actual
    trace_file = name_trace_file({
        "expected_name": "Topsy Prime",
        "actual_name": "Topsy Mirror"
    })
    assert module.flag_identity_drift(trace_file) is True

    # Case 2: identity_conflict is true
    trace_file = name_trace_file({
        "expected_name": "Echo",
        "actual_name": "Echo",
        "identity_conflict": True
    })
    assert module.flag_identity_drift(trace_file) is True

    # Case 3: no conflict, names match
    trace_file = name_trace_file({
        "expected_name": "Atlas",
        "actual_name": "Atlas"
    })
    assert module.flag_identity_drift(trace_file) is False

    # Case 4: corrupted JSON
    corrupted = trace_file.parent / "corrupted.json"
    corrupted.write_text("{ not valid json", encoding="utf-8")
    assert module.flag_identity_drift(corrupted) is False

    # Case 5: missing file
    missing = trace_file.parent / "not_here.json"
    assert module.flag_identity_drift(missing) is False
