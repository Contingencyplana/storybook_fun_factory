# Filename: test_s2_1_the_echo_stayed_within_the_thread.py

import pytest
from pathlib import Path
import re

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._2_1_the_echo_stayed_within_the_thread import (
    capture_dormant_echo,
    log_dormant_echo
)

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

    assert re.fullmatch(r"[a-f0-9\-]{36}", echo["echo_id"])
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
