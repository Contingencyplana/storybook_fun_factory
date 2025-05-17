"""
test_s3_1_it_verifies_mirrored_stanza_pairs_exist_and_match.py

Validates mirrored stanza folder comparison using mock stanza directories.
Fully dynamic and 📜 5.5-compliant.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s3_1_it_verifies_mirrored_stanza_pairs_exist_and_match import (
    verify_mirrored_stanzas,
)


def test_verify_mirrored_stanzas_file_mismatch():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)

        stanza_a = base / "stanzaA"
        stanza_b = base / "stanzaB"
        stanza_a.mkdir()
        stanza_b.mkdir()

        # Mirror registry
        mirror_registry = [
            {
                "left_stanza_path": "stanzaA",
                "right_stanza_path": "stanzaB"
            }
        ]
        registry_path = base / "mirror_pairs.json"
        with registry_path.open("w", encoding="utf-8") as f:
            json.dump(mirror_registry, f, indent=2)

        # Create mismatch files
        (stanza_a / "line1.py").write_text("A1")
        (stanza_a / "line2.py").write_text("A2")
        (stanza_b / "line1.py").write_text("B1")
        # Missing line2.py in stanzaB

        results = verify_mirrored_stanzas(str(registry_path), str(base))
        assert len(results) == 1
        assert results[0]["reason"] == "File mismatch"
        assert "line2.py" in results[0]["left_files"]
        assert "line2.py" not in results[0]["right_files"]
