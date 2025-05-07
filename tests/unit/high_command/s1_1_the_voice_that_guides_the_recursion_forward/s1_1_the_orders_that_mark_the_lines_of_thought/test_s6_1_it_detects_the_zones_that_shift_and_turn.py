"""
Test File: test_6_1_it_detects_the_zones_that_shift_and_turn.py
Tests the logic of s6_1_it_detects_the_zones_that_shift_and_turn.py
Ensures recent activity detection and directory scanning functions work as intended.
"""

import tempfile
import time
from pathlib import Path

from high_command.s1_1_the_orders_that_mark_the_lines_of_thought import s6_1_it_detects_the_zones_that_shift_and_turn as zone_detector


def create_temp_file(path: Path, age_seconds: int = 0) -> Path:
    """Create a temporary file and optionally backdate its modification time."""
    path.write_text("Test content.")
    if age_seconds > 0:
        past_time = time.time() - age_seconds
        os.utime(path, (past_time, past_time))
    return path


def test_detects_recent_activity():
    """Tests that the system detects recently modified files within the time threshold."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        root = Path(tmpdirname)
        subfolder = root / "test_zone"
        subfolder.mkdir()

        recent_file = create_temp_file(subfolder / "recent.py")
        old_file = create_temp_file(subfolder / "stale.py", age_seconds=60 * 60 * 72)  # 72 hours old

        results = zone_detector.scan_for_active_zones(root, threshold_seconds=60 * 60 * 48)  # 48 hours

        zone_key = "test_zone"
        assert zone_key in results
        assert "recent.py" in results[zone_key]
        assert "stale.py" not in results[zone_key]


def test_ignores_unmonitored_extensions():
    """Tests that files with unmonitored extensions are ignored."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        root = Path(tmpdirname)
        subfolder = root / "misc_zone"
        subfolder.mkdir()

        create_temp_file(subfolder / "data.csv")  # Not a monitored extension
        results = zone_detector.scan_for_active_zones(root)

        assert "misc_zone" not in results  # Should be ignored entirely


def test_print_active_zones_report(capfd):
    """Tests the print function outputs expected lines."""
    log = {
        "alpha/zone1": ["file1.py", "file2.md"],
        "beta/zone2": ["log.json"]
    }
    zone_detector.print_active_zones_report(log)
    captured = capfd.readouterr()
    assert "alpha/zone1" in captured.out
    assert "file1.py" in captured.out
    assert "beta/zone2" in captured.out
    assert "log.json" in captured.out
