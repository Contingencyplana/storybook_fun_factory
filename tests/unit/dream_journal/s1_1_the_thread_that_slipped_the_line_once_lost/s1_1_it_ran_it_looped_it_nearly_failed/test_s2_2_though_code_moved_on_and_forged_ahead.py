# Filename: test_s2_2_though_code_moved_on_and_forged_ahead.py

import pytest
from pathlib import Path
import re

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._2_2_though_code_moved_on_and_forged_ahead import (
    document_skipped_signal,
    log_resilient_progress
)

def test_document_skipped_signal_creates_valid_structure():
    """
    Ensures the skipped signal record contains all expected keys and formatting.
    """
    signal = "undefined-link"
    context = "Encountered recursion shortcut around symbolic boundary."
    record = document_skipped_signal(signal, context)

    assert "timestamp" in record
    assert record["signal"] == signal
    assert record["context_summary"].startswith("Encountered recursion shortcut")
    assert len(record["context_hash"]) == 64
    assert re.fullmatch(r"[a-f0-9]{64}", record["context_hash"])

def test_log_resilient_progress_creates_log_entry(tmp_path):
    """
    Verifies that the resilient progress entry is written to the log file.
    """
    test_log_file = tmp_path / "logs" / "resilience_over_precision_log.txt"
    test_log_file.parent.mkdir(parents=True, exist_ok=True)

    signal = "partial-resolve"
    context = "Code moved forward despite missing feedback from symbolic trigger."
    record = document_skipped_signal(signal, context)

    log_resilient_progress(record, override_path=test_log_file)

    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Signal Skipped:" in content
    assert "Digest:" in content
    assert "Summary:" in content
