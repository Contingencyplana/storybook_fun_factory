"""
🧪 test_s1_2_it_logs_the_recursion_drift_without_interrupt.py

Tests the DriftLogger class using 📜 5.5 dynamic import methodology.
Verifies log creation, content accuracy, and non-destructive drift tracking.
"""

import os
import json
import importlib.util
import pytest
from pathlib import Path


# ✅ Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)


# ✅ Load target module dynamically
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_1_it_hears_the_anomaly_but_does_not_judge",
        "s1_2_it_logs_the_recursion_drift_without_interrupt.py"
    )
)

DriftLogger = module.DriftLogger


def test_log_drift_creates_log_entry(tmp_path, monkeypatch):
    # ✅ Redirect Path.cwd() to temporary directory
    monkeypatch.setattr("pathlib.Path.cwd", lambda: tmp_path)

    logger = DriftLogger()
    logger.log_drift(
        trace_id="loop-test-002",
        observed="A → D → E → A",
        baseline="A → B → C → A"
    )

    log_file = tmp_path / "quarantine_logs" / "recursion_drift_log.jsonl"
    assert log_file.exists()

    with log_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 1
    data = json.loads(lines[0])
    assert data["trace_id"] == "loop-test-002"
    assert data["observed"] == "A → D → E → A"
    assert data["baseline"] == "A → B → C → A"
    assert data["status"] == "logged_without_interrupt"
    assert "timestamp" in data
