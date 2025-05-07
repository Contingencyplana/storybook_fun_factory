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
    Heuristically determines the 'type' of a zone based on the filenames present.
    Possible types:
    - creative: Presence of .md or content files
    - testing: Presence of test_*.py
    - failing: Presence of failure markers (e.g., failed_test.log)
    - stalled: Only old files or no meaningful activity
    - mixed: More than one clear type
    """
    types_detected = set()

    for filename in file_list:
        if filename.endswith(".md") or filename.endswith(".txt"):
            types_detected.add("creative")
        elif re.match(r"test_.*\.py", filename):
            types_detected.add("testing")
        elif "fail" in filename or filename.endswith(".log"):
            types_detected.add("failing")

    if not types_detected:
        return "stalled"
    elif len(types_detected) == 1:
        return types_detected.pop()
    else:
        return "mixed"


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
