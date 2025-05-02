"""
Filename: test_s2_3_four_lines_remain_their_truth_restored.py
(Tests for the restoration of discarded logic fragments in dream_journal)

This suite validates fragment recovery and structured JSONL logging
from s2_3_four_lines_remain_their_truth_restored.py using dynamic import.
"""

import os
import importlib.util
import json
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
        "s2_3_four_lines_remain_their_truth_restored.py",
    )
)

# Access the functions
restore_discarded_fragment = module.restore_discarded_fragment
log_restored_truth = module.log_restored_truth


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
