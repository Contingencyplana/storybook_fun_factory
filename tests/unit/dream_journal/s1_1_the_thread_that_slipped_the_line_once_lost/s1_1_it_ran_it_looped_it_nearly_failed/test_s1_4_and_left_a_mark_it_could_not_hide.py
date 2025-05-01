# Filename: test_s1_4_and_left_a_mark_it_could_not_hide.py

import pytest
from pathlib import Path
import re
from datetime import datetime

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._1_4_and_left_a_mark_it_could_not_hide import (
    create_permanent_trace,
    log_permanent_trace
)

def test_create_permanent_trace_structure_and_signature():
    """
    Verifies that the permanent trace dictionary includes all required fields and a valid SHA-256 signature.
    """
    description = "Unexpected echo across stanzas"
    trace = create_permanent_trace(description)

    assert "timestamp" in trace
    assert "description" in trace
    assert "mark_id" in trace
    assert "signature" in trace

    assert trace["description"] == description
    assert re.fullmatch(r"[a-f0-9\-]{36}", trace["mark_id"])
    assert re.fullmatch(r"[a-f0-9]{64}", trace["signature"])

def test_log_permanent_trace_creates_log_entry(tmp_path):
    """
    Confirms that a permanent trace entry is written to the specified log file.
    """
    test_log_file = tmp_path / "logs" / "permanent_trace_log.txt"
    test_log_file.parent.mkdir(parents=True, exist_ok=True)

    description = "Nested choice led to null state loop"
    trace = create_permanent_trace(description)
    log_permanent_trace(trace, override_path=test_log_file)

    assert test_log_file.exists()
    log_content = test_log_file.read_text()
    assert "Trace:" in log_content
    assert "Signature:" in log_content
    assert "Mark ID:" in log_content
