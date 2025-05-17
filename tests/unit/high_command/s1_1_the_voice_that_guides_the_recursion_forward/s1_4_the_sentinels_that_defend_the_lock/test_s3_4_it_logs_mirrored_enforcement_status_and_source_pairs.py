"""
test_s3_4_it_logs_mirrored_enforcement_status_and_source_pairs.py

Validates that mirror stanza status records are logged in JSONL format correctly.
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s3_4_it_logs_mirrored_enforcement_status_and_source_pairs import (
    log_mirror_status,
)


def test_log_mirror_status_jsonl_output():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        log_path = base / "mirror_status.jsonl"

        summary = [
            {
                "pair": {"left": "stanzaA", "right": "stanzaB"},
                "status": "passed"
            },
            {
                "pair": {"left": "stanzaX", "right": "stanzaY"},
                "status": "failed",
                "notes": "Shape mismatch on line2.py"
            }
        ]

        log_mirror_status(summary, str(log_path))

        assert log_path.exists()
        lines = log_path.read_text().splitlines()
        assert len(lines) == 2

        entry1 = json.loads(lines[0])
        entry2 = json.loads(lines[1])

        assert entry1["status"] == "passed"
        assert entry2["status"] == "failed"
        assert "notes" in entry2
        assert entry2["left_stanza_path"] == "stanzaX"
