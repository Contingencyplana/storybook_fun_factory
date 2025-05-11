"""
Test for s2_1_it_detects_the_break_before_the_trace_resolves.py
Uses 📜 5.5-compliant dynamic import methodology.
"""

import os
import importlib.util
import tempfile
from pathlib import Path
import pytest


def dynamic_import_module(module_path: str, module_name: str = "dynamic_module"):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def transition_log(tmp_path):
    def _write_log(lines):
        log_file = tmp_path / "transition_log.txt"
        log_file.write_text("\n".join(lines), encoding="utf-8")
        return log_file
    return _write_log


def test_detects_break_on_abort_or_missing_trace(transition_log):
    # Dynamically import target module
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_2_the_transitions_that_shape_the_recursive_path/cycle_1_guided_passage_between_worlds/s2_1_it_detects_the_break_before_the_trace_resolves.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Scenario 1: HANDOFF_INITIATED but no CANONICAL_TRACE_LINKED
    log_file = transition_log(["HANDOFF_INITIATED", "SOME_EVENT"])
    assert module.detect_mid_transition_break(log_file) is True

    # Scenario 2: HANDOFF_INITIATED followed by HANDOFF_ABORTED
    log_file = transition_log(["HANDOFF_INITIATED", "HANDOFF_ABORTED"])
    assert module.detect_mid_transition_break(log_file) is True

    # Scenario 3: Normal transition (initiated and linked)
    log_file = transition_log(["HANDOFF_INITIATED", "CANONICAL_TRACE_LINKED"])
    assert module.detect_mid_transition_break(log_file) is False

    # Scenario 4: No initiation
    log_file = transition_log(["CANONICAL_TRACE_LINKED"])
    assert module.detect_mid_transition_break(log_file) is False
