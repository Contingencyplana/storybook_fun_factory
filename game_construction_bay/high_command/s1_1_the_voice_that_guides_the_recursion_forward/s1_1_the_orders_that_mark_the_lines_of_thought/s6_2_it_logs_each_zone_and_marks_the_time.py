"""
Filename: s6_2_it_logs_each_zone_and_marks_the_time.py
Purpose: Records each active zone and its last-modified timestamp.

Part of: Cycle 3 – Active Zone Management
Stanza 1 – The Mapping of Active Zones

Dependencies: Expects input from s6_1_it_detects_the_zones_that_shift_and_turn.py,
which provides a dictionary of active zones and recently modified files.
"""

import os
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime


# Default location for storing zone logs
DEFAULT_LOG_DIR = Path("logs/zone_activity")
DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / "active_zones.json"


def get_latest_modification_time(folder_path: Path, filenames: List[str]) -> str:
    """
    Returns the most recent modification time (ISO format) among the provided files in the folder.
    """
    latest_timestamp = 0
    for filename in filenames:
        file_path = folder_path / filename
        if file_path.exists():
            ts = file_path.stat().st_mtime
            if ts > latest_timestamp:
                latest_timestamp = ts

    return datetime.fromtimestamp(latest_timestamp).isoformat() if latest_timestamp else ""


def build_timestamp_log(
    root_dir: Path,
    zone_file_map: Dict[str, List[str]]
) -> Dict[str, str]:
    """
    Builds a dictionary mapping each zone to its latest modification timestamp.
    """
    timestamp_log = {}
    for relative_path, files in zone_file_map.items():
        full_path = root_dir / relative_path
        timestamp = get_latest_modification_time(full_path, files)
        if timestamp:
            timestamp_log[relative_path] = timestamp
    return timestamp_log


def save_timestamp_log(log_data: Dict[str, str], output_path: Path = DEFAULT_LOG_FILE):
    """
    Writes the zone timestamp log to a JSON file for persistence and downstream logic.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)
    print(f"✅ Zone timestamp log saved to: {output_path.resolve()}")


if __name__ == "__main__":
    # EXAMPLE ONLY: in real usage, this script is called by a larger pipeline.
    # Simulate zone data for demonstration purposes
    sample_zone_file_map = {
        "high_command/sample_zone": ["recent.py", "notes.md"]
    }
    root = Path(__file__).resolve().parents[4]  # Adjust depth as needed
    log = build_timestamp_log(root, sample_zone_file_map)
    save_timestamp_log(log)
