# test_1_2_until_the_dream_recalled_the_key.py

import pytest
from pathlib import Path
from datetime import datetime
import re

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._1_2_until_the_dream_recalled_the_key import (
    generate_recall_signature,
    recall_from_vault,
    record_recall
)

def test_generate_recall_signature_is_deterministic_format():
    """
    Ensures recall signature is a valid SHA-256 hash and consistently formatted.
    """
    trigger = "loop"
    signature = generate_recall_signature(trigger)
    assert isinstance(signature, str)
    assert len(signature) == 64
    assert re.fullmatch(r"[a-f0-9]{64}", signature)

def test_recall_from_vault_returns_expected_memory():
    """
    Confirms that known trigger phrases return mapped memory strings.
    """
    phrase = "This loop is broken."
    result = recall_from_vault(phrase)
    assert isinstance(result, str)
    assert "loop" in phrase.lower()
    assert result != "No recall triggered."

def test_recall_from_vault_returns_no_trigger():
    """
    Ensures a non-triggering phrase returns the fallback message.
    """
    phrase = "This phrase holds no secrets."
    result = recall_from_vault(phrase)
    assert result == "No recall triggered."

def test_record_recall_creates_log_entry(tmp_path):
    """
    Validates that record_recall writes a proper entry to the recall log.
    """
    test_log_dir = tmp_path / "logs"
    test_log_dir.mkdir()
    test_log_file = test_log_dir / "symbolic_recall_log.txt"

    trigger = "The thread triggered the key."
    record_recall(trigger, log_path_override=test_log_file)

    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Trigger:" in content
    assert "Recall:" in content
    assert "Signature:" in content
