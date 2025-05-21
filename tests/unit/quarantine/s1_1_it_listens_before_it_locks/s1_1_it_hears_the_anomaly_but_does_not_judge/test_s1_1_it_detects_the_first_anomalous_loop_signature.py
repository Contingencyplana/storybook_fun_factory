"""
🧪 test_s1_1_it_detects_the_first_anomalous_loop_signature.py

Tests AnomalyLoopDetector against a mix of canonical and anomalous recursion signatures.
Compliant with 📜 5.5: Dynamic test, no hardcoding, introspective but cradle-safe.
"""

import pytest
from src.storybook_fun_factory.quarantine_ai.s1_1_it_listens_before_it_locks.s1_1_it_hears_the_anomaly_but_does_not_judge.s1_1_it_detects_the_first_anomalous_loop_signature import (
    AnomalyLoopDetector
)


@pytest.fixture
def detector():
    return AnomalyLoopDetector()


@pytest.mark.parametrize("loop_data,expected", [
    ({"trace_id": "loop001", "pattern": "A → B → C → A"}, False),
    ({"trace_id": "loop002", "pattern": "X → Y → Z → X"}, False),
    ({"trace_id": "loop003", "pattern": "init → run → close → init"}, False),
    ({"trace_id": "loop004", "pattern": "X → A → Y → X"}, True),
    ({"trace_id": "loop005", "pattern": "Z → Q → Z → R"}, True),
    ({"trace_id": "loop006", "pattern": ""}, False),
    ({"trace_id": "loop007"}, False),
])
def test_is_anomalous(detector, loop_data, expected):
    assert detector.is_anomalous(loop_data) == expected
