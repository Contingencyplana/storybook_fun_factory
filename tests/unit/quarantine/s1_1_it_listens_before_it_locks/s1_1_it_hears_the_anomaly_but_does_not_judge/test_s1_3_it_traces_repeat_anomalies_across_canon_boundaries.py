"""
🧪 test_s1_3_it_traces_repeat_anomalies_across_canon_boundaries.py

Tests the AnomalyRepetitionTracker class using 📜 5.5-compliant dynamic import.
Confirms ability to record and detect repeated anomaly patterns over time.
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


# ✅ Dynamically load target module
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_1_it_hears_the_anomaly_but_does_not_judge",
        "s1_3_it_traces_repeat_anomalies_across_canon_boundaries.py"
    )
)

AnomalyRepetitionTracker = module.AnomalyRepetitionTracker


def test_repetition_tracking():
    tracker = AnomalyRepetitionTracker()

    anomaly_id = "loop-ripple-007"
    assert not tracker.is_repeated(anomaly_id)

    tracker.record_occurrence(anomaly_id)
    assert not tracker.is_repeated(anomaly_id)

    tracker.record_occurrence(anomaly_id)
    assert tracker.is_repeated(anomaly_id)

    # Adding a third occurrence still returns True
    tracker.record_occurrence(anomaly_id)
    assert tracker.is_repeated(anomaly_id)

    # Different ID should be independent
    new_id = "echo-anomaly-999"
    assert not tracker.is_repeated(new_id)
