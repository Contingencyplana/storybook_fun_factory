"""
test_s2_4_it_updates_registry_with_all_flagged_breach_events.py

Tests that breach events are correctly written to a .jsonl file with timestamp and trace lineage (if present).
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s2_4_it_updates_registry_with_all_flagged_breach_events import (
    log_breach_events,
)


def test_log_breach_events_jsonl_format():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        breach_log = base / "breach_log.jsonl"

        # Prepare test metadata
        flagged_file = base / "tampered.py"
        flagged_file.write_text("print('oops')")

        meta = flagged_file.with_suffix(".meta.json")
        meta.write_text(
            json.dumps(
                {
                    "file_id": "xyz",
                    "trace_lineage": {
                        "cycle": "recursion_enforcement_protocols",
                        "stanza": "stanza_2",
                        "line": "s2_4",
                    },
                },
                indent=2,
            )
        )

        # Log an event
        events = [
            {
                "filename": "tampered.py",
                "reason": "Detected trace discrepancy",
            }
        ]

        log_breach_events(events, str(breach_log), str(base))

        # Validate that file exists and contains the expected fields
        assert breach_log.exists()
        lines = breach_log.read_text().splitlines()
        assert len(lines) == 1

        entry = json.loads(lines[0])
        assert entry["filename"] == "tampered.py"
        assert "timestamp" in entry
        assert "reason" in entry
        assert "trace_lineage" in entry
        assert entry["trace_lineage"]["line"] == "s2_4"
