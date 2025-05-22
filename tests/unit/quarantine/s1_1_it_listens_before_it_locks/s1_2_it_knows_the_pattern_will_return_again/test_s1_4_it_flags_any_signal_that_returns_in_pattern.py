"""
🧪 test_s1_4_it_flags_any_signal_that_returns_in_pattern.py
-----------------------------------------------------------
Tests pattern recurrence detection via threshold flagging (📜 5.5-compliant).
"""

import os
import json
import pytest
import importlib.util

# 📦 Load the dynamic_importer helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# 📄 Load the target stanza file dynamically
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s1_4_it_flags_any_signal_that_returns_in_pattern.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_flags_signals_that_repeat(tmp_path):
    log_file = tmp_path / "echoes.jsonl"
    entries = [
        {"signal": "loop_alpha"},
        {"signal": "loop_beta"},
        {"signal": "loop_alpha"},
        {"signal": "loop_alpha"},
        {"signal": "loop_gamma"},
        {"signal": "loop_beta"},
    ]
    with open(log_file, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")

    results = module.flag_repeating_signals(log_file, threshold=2)
    result_signals = [r["signal"] for r in results]

    assert set(result_signals) == {"loop_alpha", "loop_beta"}
