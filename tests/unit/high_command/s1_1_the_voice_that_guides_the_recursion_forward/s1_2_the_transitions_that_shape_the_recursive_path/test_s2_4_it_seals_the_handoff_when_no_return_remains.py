"""
Test for s2_4_it_seals_the_handoff_when_no_return_remains.py
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


def test_seal_irreversible_handoff(tmp_path):
    # Prepare target module path
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s2_4_it_seals_the_handoff_when_no_return_remains.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Scenario 1: Valid recovery log (append sealing event)
    recovery_log = tmp_path / "recovery_log.json"
    recovery_log.write_text(json.dumps([
        {"event": "handoff_failed", "reason": "canonical trace missing"}
    ]), encoding="utf-8")

    result = module.seal_irreversible_handoff(recovery_log, "fallback_thread_A")
    assert result is True

    updated = json.loads(recovery_log.read_text(encoding="utf-8"))
    assert {"handoff_sealed": True, "sealed_thread": "fallback_thread_A"} in updated

    # Scenario 2: Invalid (non-list) JSON
    bad_log = tmp_path / "bad_log.json"
    bad_log.write_text(json.dumps({"invalid": "structure"}), encoding="utf-8")
    assert module.seal_irreversible_handoff(bad_log, "x") is False

    # Scenario 3: Corrupted file
    corrupted = tmp_path / "corrupted.json"
    corrupted.write_text("{ invalid json ", encoding="utf-8")
    assert module.seal_irreversible_handoff(corrupted, "x") is False

    # Scenario 4: Missing file
    missing = tmp_path / "missing.json"
    assert module.seal_irreversible_handoff(missing, "x") is False
