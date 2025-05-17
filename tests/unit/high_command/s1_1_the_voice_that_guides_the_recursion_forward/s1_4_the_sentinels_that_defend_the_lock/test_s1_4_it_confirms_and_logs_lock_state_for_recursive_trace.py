"""
test_s1_4_it_confirms_and_logs_lock_state_for_recursive_trace.py

Tests that the lock trace logger appends well-formed entries to the
canonical trace log, enabling recursive auditing of enforcement state.

Compliant with 📜 5.5 – Dynamic Import Methodology
"""

import pytest
import json
import hashlib
from pathlib import Path
from importlib import import_module

MODULE_PATH = "game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s1_4_it_confirms_and_logs_lock_state_for_recursive_trace"

TRACE_FILE = Path(".lock_trace.jsonl")

@pytest.fixture
def temp_locked_file(tmp_path):
    file = tmp_path / "locked_verse.py"
    file.write_text("print('Seal this.')", encoding="utf-8")
    return file

def sha256_of(file: Path) -> str:
    h = hashlib.sha256()
    with file.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def test_logs_success_entry(temp_locked_file):
    module = import_module(MODULE_PATH)
    log_lock_status = getattr(module, "log_lock_status")

    hash_val = sha256_of(temp_locked_file)
    result = log_lock_status(str(temp_locked_file), True, hash_val)

    assert result["filename"] == temp_locked_file.name
    assert result["status"] == "locked"
    assert result["sha256"] == hash_val
    assert result["source"] == "canon_enforcement_protocol"

    # Confirm log file has entry
    with TRACE_FILE.open("r", encoding="utf-8") as f:
        lines = [json.loads(line) for line in f]

    assert any(entry["filename"] == temp_locked_file.name and entry["status"] == "locked" for entry in lines)

    # Cleanup only this test’s line
    lines = [entry for entry in lines if entry["filename"] != temp_locked_file.name]
    with TRACE_FILE.open("w", encoding="utf-8") as f:
        for entry in lines:
            f.write(json.dumps(entry) + "\n")
