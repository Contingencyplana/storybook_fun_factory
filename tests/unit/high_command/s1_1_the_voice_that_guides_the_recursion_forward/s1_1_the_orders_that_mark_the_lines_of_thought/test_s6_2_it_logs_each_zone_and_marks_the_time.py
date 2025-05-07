"""
Test File: test_s6_2_it_logs_each_zone_and_marks_the_time.py
Tests the logic of s6_2_it_logs_each_zone_and_marks_the_time.py
Verifies that zone timestamps are correctly calculated and saved.
"""

import os
import json
import time
import tempfile
from pathlib import Path
from datetime import datetime

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s6_2_it_logs_each_zone_and_marks_the_time as zone_logger


def test_build_timestamp_log_recognizes_latest_file():
    """Ensure the log correctly identifies the most recently modified file in a zone."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        root = Path(tmpdirname)
        zone_path = root / "alpha_zone"
        zone_path.mkdir()

        # Create an old file and a recent file
        old_file = zone_path / "old_script.py"
        old_file.write_text("old")
        os.utime(old_file, (time.time() - 10000, time.time() - 10000))  # 10,000s ago

        new_file = zone_path / "new_script.py"
        new_file.write_text("new")
        time.sleep(1)  # Ensure mtime separation
        os.utime(new_file, None)  # Current time

        zone_file_map = {
            "alpha_zone": ["old_script.py", "new_script.py"]
        }

        result = zone_logger.build_timestamp_log(root, zone_file_map)
        assert "alpha_zone" in result

        timestamp_str = result["alpha_zone"]
        ts = datetime.fromisoformat(timestamp_str)
        now = datetime.now()

        assert (now - ts).total_seconds() < 10  # Should be recent


def test_save_timestamp_log_writes_json_file():
    """Ensure the log is correctly written to JSON."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        log_data = {
            "beta_zone": datetime.now().isoformat()
        }
        output_file = Path(tmpdirname) / "test_log.json"
        zone_logger.save_timestamp_log(log_data, output_path=output_file)

        assert output_file.exists()
        with open(output_file, "r", encoding="utf-8") as f:
            loaded = json.load(f)

        assert loaded == log_data


def test_empty_log_skips_zones_with_no_valid_timestamps():
    """Ensure that zones with no valid files do not appear in the log."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        root = Path(tmpdirname)
        zone_path = root / "ghost_zone"
        zone_path.mkdir()

        # Supply a filename that doesn't exist
        zone_file_map = {
            "ghost_zone": ["missing.py"]
        }

        result = zone_logger.build_timestamp_log(root, zone_file_map)
        assert result == {}  # Should skip zones with no timestamps
