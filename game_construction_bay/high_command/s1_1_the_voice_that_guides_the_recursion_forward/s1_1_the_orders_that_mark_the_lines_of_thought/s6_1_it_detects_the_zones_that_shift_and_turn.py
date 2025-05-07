"""
Filename: s6_1_it_detects_the_zones_that_shift_and_turn.py
Purpose: Scans all folders in the recursive project structure to detect recent activity such as:
- New file creations
- File modifications
- Failed test logs
- Other signs of creative or recursive motion

Part of: Cycle 3 – Active Zone Management
Stanza 1 – The Mapping of Active Zones
"""

import os
import time
from pathlib import Path
from typing import List, Dict


# Define which file extensions and subfolders to monitor
MONITORED_EXTENSIONS = {'.py', '.md', '.json'}
IGNORED_DIRS = {'__pycache__', '.git', '.venv', '.mypy_cache'}

# Activity threshold in seconds (e.g., 2 days)
DEFAULT_ACTIVITY_WINDOW = 60 * 60 * 48


def is_recent(path: Path, threshold_seconds: int) -> bool:
    """Return True if file was modified within threshold."""
    return (time.time() - path.stat().st_mtime) <= threshold_seconds


def scan_for_active_zones(
    root_dir: Path,
    threshold_seconds: int = DEFAULT_ACTIVITY_WINDOW
) -> Dict[str, List[str]]:
    """
    Traverse the given root directory recursively,
    returning a dict mapping zone paths to lists of recently modified files.
    """
    activity_log = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Ignore irrelevant folders
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        relative_path = os.path.relpath(dirpath, root_dir)

        # Track only zones with recent activity
        recent_files = []
        for file in filenames:
            file_path = Path(dirpath) / file
            if file_path.suffix in MONITORED_EXTENSIONS and is_recent(file_path, threshold_seconds):
                recent_files.append(file_path.name)

        if recent_files:
            activity_log[relative_path] = recent_files

    return activity_log


def print_active_zones_report(activity_log: Dict[str, List[str]]):
    """Prints a human-readable summary of detected active zones."""
    if not activity_log:
        print("No recent activity detected in any monitored zones.")
        return

    print("📍 Detected Active Zones:\n")
    for zone, files in activity_log.items():
        print(f"🗂️  {zone}/")
        for f in files:
            print(f"    └─ 📝 {f}")
        print()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]  # Adjust depth as needed
    log = scan_for_active_zones(project_root)
    print_active_zones_report(log)
