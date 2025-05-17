"""
test_s2_2_it_identifies_unsanctioned_timestamp_or_commit.py

Tests timestamp-based enforcement of modified files using a canonical registry.
Git checks are skipped in this test for simplicity and portability.
Fully dynamic and 📜 5.5 compliant.
"""

import json
import time
from pathlib import Path
from tempfile import TemporaryDirectory

from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s2_2_it_identifies_unsanctioned_timestamp_or_commit import (
    detect_timestamp_and_git_anomalies,
)


def test_detect_timestamp_anomalies_only():
    with TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        file1 = base / "file1.py"
        file1.write_text("stable content")

        # Timestamp is BEFORE current time to simulate safe file
        canonical_time = (file1.stat().st_mtime) + 5

        registry = {
            "file1.py": (
                str((Path(file1).stat().st_mtime))
            )
        }

        registry_path = base / "timestamp_registry.json"
        with registry_path.open("w", encoding="utf-8") as f:
            json.dump(
                {"file1.py": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(file1.stat().st_mtime))},
                f,
                indent=2,
            )

        # Now simulate tampering
        time.sleep(1)
        file1.write_text("tampered content")

        flagged = detect_timestamp_and_git_anomalies(
            str(registry_path), str(base)
        )

        assert "file1.py" in flagged
