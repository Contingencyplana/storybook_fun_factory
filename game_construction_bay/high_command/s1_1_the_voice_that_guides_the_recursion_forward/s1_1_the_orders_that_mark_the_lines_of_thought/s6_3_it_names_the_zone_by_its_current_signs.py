"""
Filename: s6_3_it_names_the_zone_by_its_current_signs.py
Purpose: Assigns a type to each zone (e.g., creative, testing, failing, stalled)
based on file names, recent activity, and common recursion patterns.

Part of: Cycle 3 – Active Zone Management
Stanza 1 – The Mapping of Active Zones
"""

import re
from typing import Dict, List


def classify_zone(file_list: List[str]) -> str:
    """
    Assigns a type to the zone based on its files, prioritizing:
    1. failing > 2. testing > 3. creative > 4. stalled
    """
    has_failing = False
    has_testing = False
    has_creative = False

    for filename in file_list:
        # More robust detection for failure indicators
        if re.search(r"(fail|error)", filename, re.IGNORECASE) or filename.endswith(".log"):
            has_failing = True
        if re.match(r"test_.*\.py", filename):
            has_testing = True
        if filename.endswith(".md") or filename.endswith(".txt"):
            has_creative = True

    if has_failing:
        return "failing"
    elif has_testing:
        return "testing"
    elif has_creative:
        return "creative"
    else:
        return "stalled"


def assign_zone_types(zone_file_map: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Given a mapping of zone paths to file lists, returns a mapping of
    zone paths to their classified zone type.
    """
    return {
        zone: classify_zone(files)
        for zone, files in zone_file_map.items()
    }


if __name__ == "__main__":
    # Example usage
    sample = {
        "alpha": ["main.py", "notes.md"],
        "beta": ["test_alpha.py"],
        "gamma": ["fail_log.txt", "error_report.log"],
        "delta": [],
        "epsilon": ["script.py", "test_script.py", "notes.md"]
    }

    classifications = assign_zone_types(sample)
    for zone, zone_type in classifications.items():
        print(f"{zone}: {zone_type}")
