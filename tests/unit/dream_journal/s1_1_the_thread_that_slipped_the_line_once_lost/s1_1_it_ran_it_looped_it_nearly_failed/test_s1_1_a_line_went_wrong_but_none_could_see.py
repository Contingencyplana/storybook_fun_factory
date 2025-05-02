# Filename: test_s1_1_a_line_went_wrong_but_none_could_see.py

import pytest
from pathlib import Path
from datetime import datetime
import logging
import re

from storybook_fun_factory.dream_journal.s1_1_the_thread_that_slipped_the_line_once_lost.s1_1_it_ran_it_looped_it_nearly_failed.s1_1_a_line_went_wrong_but_none_could_see import (
    detect_subtle_deviation,
    log_hidden_trace,
    process_anomalies
)

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

    # Patch Path.cwd() so the module writes logs to our tmp_path
    monkeypatch.setattr("pathlib.Path.cwd", lambda: tmp_path)

    # Use a dedicated logger to avoid interfering with global logging state
    logger = logging.getLogger("test_hidden_trace_logger")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(test_log_file)
    handler.setFormatter(logging.Formatter("%(message)s"))

    # Clear and configure only our logger
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)

    # Prepare test anomalies
    test_anomalies = [
        {"id": "test_001", "timestamp": datetime(2025, 4, 20, 8, 0, 0), "pattern": "loop-glitch"},
        {"id": "test_002", "timestamp": datetime(2025, 4, 20, 8, 1, 0), "pattern": "echo-fade"},
    ]

    # Call the real function, which will now write logs to test_log_file due to monkeypatch
    process_anomalies(test_anomalies)

    # Validate output
    assert test_log_file.exists()
    log_content = test_log_file.read_text()
    assert "loop-glitch" in log_content
    assert "echo-fade" in log_content
    assert len(re.findall("Hidden fault detected", log_content)) == 2
