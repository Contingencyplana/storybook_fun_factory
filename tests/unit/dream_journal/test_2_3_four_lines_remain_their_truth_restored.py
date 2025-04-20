# test_2_3_four_lines_remain_their_truth_restored.py

import pytest
from pathlib import Path
import json
import re

from storybook_fun_factory.dream_journal._1_1_the_thread_that_slipped_the_line_once_lost._1_1_it_ran_it_looped_it_nearly_failed._2_3_four_lines_remain_their_truth_restored import (
    restore_discarded_fragment,
    log_restored_truth
)

def test_restore_discarded_fragment_structure_and_hash():
    """
    Ensures that a logic fragment is correctly converted into a structured restoration record with valid hash.
    """
    code = "if dream.loop(): yield"
    origin = "fragment_22"
    result = restore_discarded_fragment(code, origin)

    assert isinstance(result, dict)
    assert result["fragment_code"] == code
    assert result["origin_trace"] == origin
    assert "timestamp" in result
    assert "fragment_id" in result
    assert re.fullmatch(r"[a-f0-9]{64}", result["fragment_id"])

def test_log_restored_truth_creates_valid_json_line(tmp_path):
    """
    Verifies that a restored truth fragment is properly written to a JSONL log file.
    """
    log_file = tmp_path / "logs" / "truth_restoration_log.jsonl"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    fragment = "return if thread.rebind()"
    origin = "echo-deviation-7"
    record = restore_discarded_fragment(fragment, origin)

    log_restored_truth(record, override_path=log_file)

    assert log_file.exists()

    with log_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 1
        loaded = json.loads(lines[0])
        assert loaded["fragment_code"] == fragment
        assert loaded["origin_trace"] == origin
        assert re.fullmatch(r"[a-f0-9]{64}", loaded["fragment_id"])
