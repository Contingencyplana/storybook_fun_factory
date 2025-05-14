# File: s5_3_if_hot_zones_wait_it_gives_priority.py

"""
s5_3_if_hot_zones_wait_it_gives_priority.py

Prioritizes dispatch toward files located in designated "hot zones"—critical paths
or urgent components that require accelerated recursive attention. This logic helps
High Command assign focus to areas under pressure or strategic necessity.
"""

import os
from pathlib import Path

HOT_ZONE_KEYWORDS = ["test_suites", "recursion_renders", "high_priority", "active_zone"]

def is_hot_zone_path(file_path: str) -> bool:
    """
    Returns True if the given path contains any of the predefined hot zone keywords.
    """
    return any(keyword in file_path for keyword in HOT_ZONE_KEYWORDS)

def list_hot_zone_files(directory: str, include_tests: bool = False) -> list[str]:
    """
    Scans the directory for files in hot zones and returns a prioritized list.
    Optionally includes test files if 'include_tests' is True.
    """
    hot_zone_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(".py"):
                continue
            if not include_tests and file.startswith("test_"):
                continue
            full_path = os.path.join(root, file)
            if is_hot_zone_path(full_path):
                hot_zone_files.append(full_path)

    return sorted(hot_zone_files)
