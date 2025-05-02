"""
Filename: test_s1_1_a_line_went_wrong_but_none_could_see.py
(Tests for detecting hidden recursive deviations in dream_journal)

This file tests the anomaly detection and poetic logging of subtle recursive faults
within s1_1_a_line_went_wrong_but_none_could_see.py using dynamic import.
"""

import os
import importlib.util
import logging
import re
from datetime import datetime
import pytest

# Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza module under test
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        "src",
        "storybook_fun_factory",
        "dream_journal",
        "s1_1_the_thread_that_slipped_the_line_once_lost",
        "s1_1_it_ran_it_looped_it_nearly_failed",
        "s1_1_a_line_went_wrong_but_none_could_see.py",
    )
)

# Access the functions
detect_subtle_deviation = module.detect_subtle_deviation
log_hidden_trace = module.log_hidden_trace
process_anomalies = module.process_anomalies


def test_detect_subtle_deviation_consistency():
    """
    Ensures the hash generated for the same anomaly input is consistent.
    """
    sample_anomaly = {
        "id": "dev_007",
        "timestamp": datetime(2025, 4, 20, 8, 0, 0),
        "pattern": "echo-fracture"
    }
    first_hash = detect_subtle_deviation(sample_anomaly)
    second_hash = detect_subtle_deviation(sample_anomaly)
    assert first_hash == second_hash
    assert isinstance(first_hash, str)
    assert len(first_hash) == 64


def test_process_anomalies_creates_log(tmp_path, monkeypatch):
    """
    Tests that log entries are created for each anomaly and written to file.
    """
    test_log_dir = tmp_path / "logs"
    test_log_dir.mkdir()
    test_log_file = test_log_dir / "hidden_trace_log.txt"

    # Patch Path.cwd() to redirect logging output
    monkeypatch.setattr("pathlib.Path.cwd", lambda: tmp_path)

    # Reset and configure logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=test_log_file, level=logging.INFO, format="%(message)s")

    test_anomalies = [
        {"id": "test_001", "timestamp": datetime(2025, 4, 20, 8, 0, 0), "pattern": "loop-glitch"},
        {"id": "test_002", "timestamp": datetime(2025, 4, 20, 8, 1, 0), "pattern": "echo-fade"},
    ]

    process_anomalies(test_anomalies)

    assert test_log_file.exists()
    log_content = test_log_file.read_text()
    assert "loop-glitch" in log_content
    assert "echo-fade" in log_content
    assert len(re.findall("Hidden fault detected", log_content)) == 2
