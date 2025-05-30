"""
🧪 test_s1_4_it_prepares_the_cradle_trace_for_topsy_review.py

Tests CradleTracePreparer using 📜 5.5 dynamic import strategy.
Confirms that drift logs are summarized correctly into a cradle review file.
"""

import os
import json
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
        "s1_4_it_prepares_the_cradle_trace_for_topsy_review.py"
    )
)

CradleTracePreparer = module.CradleTracePreparer


def test_cradle_trace_summary(tmp_path, monkeypatch):
    # ✅ Redirect to temp dir
    monkeypatch.setattr("pathlib.Path.cwd", lambda: tmp_path)

    log_dir = tmp_path / "quarantine_logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # ✅ Simulate 2 drift log entries
    drift_log = log_dir / "recursion_drift_log.jsonl"
    with drift_log.open("w", encoding="utf-8") as f:
        f.write(json.dumps({
            "trace_id": "T-001",
            "observed": "A → D → A",
            "baseline": "A → B → C → A",
            "status": "logged_without_interrupt"
        }) + "\n")
        f.write(json.dumps({
            "trace_id": "T-002",
            "observed": "X → Y → A → X",
            "baseline": "X → Y → Z → X",
            "status": "logged_without_interrupt"
        }) + "\n")

    # ✅ Generate trace summary
    preparer = CradleTracePreparer()
    preparer.prepare_trace()

    output = preparer.load_trace_summary()
    assert "timestamp" in output
    assert isinstance(output["entries"], list)
    assert len(output["entries"]) == 2
    assert output["entries"][0]["trace_id"] == "T-001"
