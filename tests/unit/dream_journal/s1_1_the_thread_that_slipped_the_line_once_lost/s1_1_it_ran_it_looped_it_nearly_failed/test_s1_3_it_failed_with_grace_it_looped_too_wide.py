"""
Filename: test_s1_3_it_failed_with_grace_it_looped_too_wide.py
(Tests for graceful failure logging and deviation detection in dream_journal)

This test suite verifies loop classification, signature creation, and log recording
in s1_3_it_failed_with_grace_it_looped_too_wide.py using dynamic import.
"""

import os
import importlib.util
import logging
import re
from pathlib import Path
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
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "dream_journal",
        "s1_1_the_thread_that_slipped_the_line_once_lost",
        "s1_1_it_ran_it_looped_it_nearly_failed",
        "s1_3_it_failed_with_grace_it_looped_too_wide.py",
    )
)

# Access functions and constants
detect_loop_deviation = module.detect_loop_deviation
generate_failure_signature = module.generate_failure_signature
log_failure_loop = module.log_failure_loop


def test_detect_loop_deviation_returns_graceful():
    """
    Verifies that a safe iteration count returns a graceful loop classification.
    """
    result = detect_loop_deviation("test_id_001", 2, max_safe=3)
    assert "GRACEFUL LOOP" in result


def test_detect_loop_deviation_returns_unstable():
    """
    Verifies that an unsafe iteration count returns an unstable loop classification.
    """
    result = detect_loop_deviation("test_id_002", 5, max_safe=3)
    assert "UNSTABLE LOOP" in result


def test_generate_failure_signature_format():
    """
    Ensures that the generated signature is a valid SHA-256 hex string.
    """
    signature = generate_failure_signature("test_id_003", 4)
    assert isinstance(signature, str)
    assert len(signature) == 64
    assert re.fullmatch(r"[a-f0-9]{64}", signature)


def test_log_failure_loop_creates_log_file(tmp_path, monkeypatch):
    """
    Ensures that a loop failure log entry is written to the correct file.
    """
    test_log_dir = tmp_path / "logs"
    test_log_dir.mkdir()
    test_log_file = test_log_dir / "loop_echo_log.txt"

    # Patch the module's FAILURE_LOG path
    monkeypatch.setattr(module, "FAILURE_LOG", test_log_file)

    log_failure_loop("test_id_004", 6)

    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Signature:" in content
    assert "UNSTABLE LOOP" in content or "GRACEFUL LOOP" in content
