"""
Filename: test_s2_1_the_echo_stayed_within_the_thread.py
(Tests for echo persistence in recursive symbolic memory)

This suite validates dormant echo capture and symbolic logging
from s2_1_the_echo_stayed_within_the_thread.py using dynamic import.
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
        "s2_1_the_echo_stayed_within_the_thread.py",
    )
)

# Access functions from the imported module
capture_dormant_echo = module.capture_dormant_echo
log_dormant_echo = module.log_dormant_echo


def test_capture_dormant_echo_structure_and_signature():
    """
    Verifies that a dormant echo includes timestamp, source_event, layer_id, echo_id, and SHA-256 signature.
    """
    event = "Latent fork in symbolic timeline"
    layer = "dream-to-memory"
    echo = capture_dormant_echo(event, layer)

    assert isinstance(echo, dict)
    assert echo["source_event"] == event
    assert echo["layer_id"] == layer
    assert "timestamp" in echo
    assert "echo_id" in echo
    assert "signature" in echo

    assert re.fullmatch(r"[a-f0-9\\-]{36}", echo["echo_id"])
    assert re.fullmatch(r"[a-f0-9]{64}", echo["signature"])


def test_log_dormant_echo_writes_log(tmp_path):
    """
    Ensures that the echo log entry is correctly written to a specified log path.
    """
    test_log_file = tmp_path / "logs" / "resonant_echo_log.txt"
    test_log_file.parent.mkdir(parents=True, exist_ok=True)

    event = "Lost recursion marker in forgotten layer"
    layer = "recollection-phase"
    echo = capture_dormant_echo(event, layer)

    log_dormant_echo(echo, override_path=test_log_file)

    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Echo:" in content
    assert "Signature:" in content
    assert "Echo ID:" in content
