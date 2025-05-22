"""
🧪 test_s1_3_it_records_the_echoes_that_breathe_again.py
--------------------------------------------------------
Tests echo recurrence logging for the current non-cycle structure (📜 5.5-compliant).
"""

import os
import json
import pytest
from pathlib import Path
import importlib.util

# 📦 Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# 📄 Load module dynamically (flat poem-folder structure)
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s1_3_it_records_the_echoes_that_breathe_again.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_record_echo_creates_file(tmp_path):
    echo_data = {"signal": "omega", "type": "soft-return"}
    result_path = module.record_echo(echo_data, tmp_path)

    assert result_path.exists()
    assert result_path.suffix == ".json"

    with open(result_path, 'r', encoding='utf-8') as f:
        record = json.load(f)
        assert record["echo"] == echo_data
        assert "timestamp" in record
