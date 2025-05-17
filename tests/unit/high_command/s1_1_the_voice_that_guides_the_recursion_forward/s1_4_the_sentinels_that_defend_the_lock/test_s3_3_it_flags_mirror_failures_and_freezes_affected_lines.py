"""
test_s3_3_it_flags_mirror_failures_and_freezes_affected_lines.py

Tests that mirror failure entries are correctly frozen into a newline-delimited log.
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s3_3_it_flags_mirror_failures_and_freezes_affected_lines import (
    freeze_failed_mirror_lines,
)


def test_freeze_failed_mirror_lines_writes_expected_jsonl():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        freeze_log = base / "mirror_freeze.jsonl"

        failures = [
            {
                "file": "line2.py",
                "reason": "Trace mismatch",
                "pair": {
                    "left_stanza_path": "zoneA/stanza3",
                    "right_stanza_path": "zoneB/stanza3"
                }
            }
        ]

        freeze_failed_mirror_lines(failures, str(freeze_log))

        assert freeze_log.exists()
        lines = freeze_log.read_text().splitlines()
        assert len(lines) == 1

        entry = json.loads(lines[0])
        assert entry["file"] == "line2.py"
        assert entry["reason"] == "Trace mismatch"
        assert entry["left_stanza_path"] == "zoneA/stanza3"
        assert entry["right_stanza_path"] == "zoneB/stanza3"
        assert "timestamp" in entry
