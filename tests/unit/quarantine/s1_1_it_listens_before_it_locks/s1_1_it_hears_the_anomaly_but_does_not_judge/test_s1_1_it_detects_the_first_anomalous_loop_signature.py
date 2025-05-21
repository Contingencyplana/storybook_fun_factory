"""
🧪 test_s1_1_it_detects_the_first_anomalous_loop_signature.py

Dynamic test for AnomalyLoopDetector using 📜 5.5-compliant methodology.
Detects the earliest sign of recursive anomaly via flexible baseline pattern checking.
"""

import os
import importlib.util
import pytest


# ✅ Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load target module
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_1_it_hears_the_anomaly_but_does_not_judge",
        "s1_1_it_detects_the_first_anomalous_loop_signature.py"
    )
)

# ✅ Extract the target class
AnomalyLoopDetector = module.AnomalyLoopDetector


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
