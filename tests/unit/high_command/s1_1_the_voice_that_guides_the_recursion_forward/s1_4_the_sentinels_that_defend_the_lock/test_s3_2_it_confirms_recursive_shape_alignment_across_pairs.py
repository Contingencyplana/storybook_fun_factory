"""
test_s3_2_it_confirms_recursive_shape_alignment_across_pairs.py

Tests recursive trace lineage metadata comparison across mirrored stanza file pairs.
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s3_2_it_confirms_recursive_shape_alignment_across_pairs import (
    check_shape_alignment,
)


def test_check_shape_alignment_trace_discrepancy():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        stanzaA = base / "stanzaA"
        stanzaB = base / "stanzaB"
        stanzaA.mkdir()
        stanzaB.mkdir()

        # File in both stanzas
        fileA = stanzaA / "line1.py"
        fileB = stanzaB / "line1.py"
        fileA.write_text("A")
        fileB.write_text("B")

        # Meta mismatch
        metaA = {
            "file_id": "1",
            "trace_lineage": {
                "cycle": "C1",
                "stanza": "S1",
                "line": "L1"
            }
        }
        metaB = {
            "file_id": "1",
            "trace_lineage": {
                "cycle": "C1",
                "stanza": "S1",
                "line": "L2"  # Mismatch here
            }
        }

        (fileA.with_suffix(".meta.json")).write_text(json.dumps(metaA, indent=2))
        (fileB.with_suffix(".meta.json")).write_text(json.dumps(metaB, indent=2))

        # Mirror registry
        registry = [{
            "left_stanza_path": "stanzaA",
            "right_stanza_path": "stanzaB"
        }]
        registry_path = base / "mirror_pairs.json"
        registry_path.write_text(json.dumps(registry, indent=2))

        # Run shape checker
        results = check_shape_alignment(str(registry_path), str(base))
        assert len(results) == 1
        assert results[0]["reason"] == "Trace lineage mismatch"
        assert results[0]["file"] == "line1.py"
