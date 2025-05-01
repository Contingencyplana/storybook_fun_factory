# Filename: test_s2_4_a_dream_once_lost_now_reexplored.py

import pytest
from pathlib import Path
import json
import re

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._2_4_a_dream_once_lost_now_reexplored import (
    rethread_abandoned_path,
    log_path_rediscovery
)

def test_rethread_abandoned_path_structure_and_hash():
    """
    Validates that the rediscovery record includes all required fields and valid hash/signature formatting.
    """
    signature = "symbolic.trace.from.echo"
    context = "Re-entered dream-state after shadow resolution."
    result = rethread_abandoned_path(signature, context)

    assert "timestamp" in result
    assert result["path_signature"] == signature
    assert result["original_context"] == context
    assert "context_hash" in result
    assert "rediscovery_id" in result

    assert re.fullmatch(r"[a-f0-9]{64}", result["context_hash"])
    assert re.fullmatch(r"[a-f0-9\-]{36}", result["rediscovery_id"])

def test_log_path_rediscovery_writes_json_line(tmp_path):
    """
    Ensures that rediscovered paths are correctly written to a symbolic JSONL dream log.
    """
    test_log_file = tmp_path / "logs" / "dream_reexploration_log.jsonl"
    test_log_file.parent.mkdir(parents=True, exist_ok=True)

    signature = "thread.resume(symbol.lost)"
    context = "Path retraced from memory echo at divergence point."
    record = rethread_abandoned_path(signature, context)

    log_path_rediscovery(record, override_path=test_log_file)

    assert test_log_file.exists()

    with test_log_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 1
        loaded = json.loads(lines[0])
        assert loaded["path_signature"] == signature
        assert loaded["original_context"] == context
        assert re.fullmatch(r"[a-f0-9]{64}", loaded["context_hash"])
