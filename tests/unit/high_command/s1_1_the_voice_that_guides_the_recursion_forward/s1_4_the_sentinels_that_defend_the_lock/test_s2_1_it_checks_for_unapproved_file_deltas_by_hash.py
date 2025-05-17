"""
test_s2_1_it_checks_for_unapproved_file_deltas_by_hash.py

Verifies that the function correctly flags unauthorized changes to files based on SHA-256 hash comparisons.
Fully dynamic test with temporary file creation and registry generation.

Compliant with 📜 5.5 standards.
"""

import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s2_1_it_checks_for_unapproved_file_deltas_by_hash import (
    compute_file_hash,
    detect_unapproved_hash_deltas,
)

def test_detect_unapproved_hash_deltas():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)

        # Create two test files
        file1 = base / "file1.py"
        file1.write_text("original content")

        file2 = base / "file2.py"
        file2.write_text("initial data")

        # Compute initial hashes
        registry = {
            "file1.py": compute_file_hash(file1),
            "file2.py": compute_file_hash(file2),
        }

        # Save the registry to JSON
        registry_path = base / "hash_registry.json"
        with registry_path.open("w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2)

        # Modify file2 to simulate tampering
        file2.write_text("tampered data")

        # Perform delta check
        flagged = detect_unapproved_hash_deltas(
            str(registry_path), str(base)
        )

        assert "file2.py" in flagged
        assert "file1.py" not in flagged
