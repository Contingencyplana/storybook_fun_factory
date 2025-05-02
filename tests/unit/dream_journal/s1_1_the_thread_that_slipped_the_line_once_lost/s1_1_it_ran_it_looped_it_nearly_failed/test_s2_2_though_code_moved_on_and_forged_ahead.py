"""
Filename: test_s2_2_though_code_moved_on_and_forged_ahead.py
(Tests for resilient continuation despite unresolved signals in dream_journal)

This suite validates skipped signal documentation and symbolic resilience logging
from s2_2_though_code_moved_on_and_forged_ahead.py using dynamic import.
"""

import os
import importlib.util
import re
from pathlib import Path
import pytest

# Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza module under test
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "dream_journal",
        "s1_1_the_thread_that_slipped_the_line_once_lost",
        "s1_1_it_ran_it_looped_it_nearly_failed",
        "s2_2_though_code_moved_on_and_forged_ahead.py",
    )
)

# Access the functions
document_skipped_signal = module.document_skipped_signal
log_resilient_progress = module.log_resilient_progress


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
