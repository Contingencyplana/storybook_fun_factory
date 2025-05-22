"""
🧪 test_s2_1_it_tracks_recurring_interval_frequencies_over_time.py
------------------------------------------------------------------
Tests interval detection between repeated signals using dynamic import (📜 5.5-compliant).
"""

import os
import json
import pytest
from datetime import datetime, timedelta
import importlib.util

# 📦 Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# 📄 Load module dynamically
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s2_1_it_tracks_recurring_interval_frequencies_over_time.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_compute_intervals(tmp_path):
    log_file = tmp_path / "echoes.jsonl"
    base_time = datetime.now()

    entries = [
        {"signal": "alpha", "timestamp": (base_time + timedelta(seconds=0)).isoformat()},
        {"signal": "beta", "timestamp": (base_time + timedelta(seconds=5)).isoformat()},
        {"signal": "alpha", "timestamp": (base_time + timedelta(seconds=10)).isoformat()},
        {"signal": "alpha", "timestamp": (base_time + timedelta(seconds=25)).isoformat()},
        {"signal": "beta", "timestamp": (base_time + timedelta(seconds=30)).isoformat()},
    ]

    with open(log_file, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")

    result = module.compute_intervals(log_file)

    assert "alpha" in result
    assert "beta" in result
    assert result["alpha"] == [10.0, 15.0]  # alpha: [t0→t10, t10→t25]
    assert result["beta"] == [25.0]         # beta: [t5→t30]
