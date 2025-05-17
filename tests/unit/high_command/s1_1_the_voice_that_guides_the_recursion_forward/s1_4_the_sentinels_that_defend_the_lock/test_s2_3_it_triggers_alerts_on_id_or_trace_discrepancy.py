"""
test_s2_3_it_triggers_alerts_on_id_or_trace_discrepancy.py

Verifies that discrepancies in file_id and trace_lineage metadata are properly flagged.
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s2_3_it_triggers_alerts_on_id_or_trace_discrepancy import (
    detect_id_and_trace_discrepancies,
)


def test_detect_id_and_trace_discrepancies():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)

        # Canonical registry definition
        registry = {
            "file1.py": {
                "file_id": "abc-123",
                "trace_lineage": {
                    "cycle": "recursion_enforcement_protocols",
                    "stanza": "stanza_2",
                    "line": "s2_3"
                }
            }
        }

        # Create test file and metadata
        file1 = base / "file1.py"
        file1.write_text("print('safe')")

        file1_meta = base / "file1.meta.json"
        file1_meta.write_text(json.dumps({
            "file_id": "WRONG-ID",
            "trace_lineage": {
                "cycle": "recursion_enforcement_protocols",
                "stanza": "stanza_2",
                "line": "s2_3"
            }
        }, indent=2))

        # Save registry
        registry_path = base / "trace_registry.json"
        with registry_path.open("w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2)

        flagged = detect_id_and_trace_discrepancies(
            str(registry_path), str(base)
        )

        assert "file1.py" in flagged
