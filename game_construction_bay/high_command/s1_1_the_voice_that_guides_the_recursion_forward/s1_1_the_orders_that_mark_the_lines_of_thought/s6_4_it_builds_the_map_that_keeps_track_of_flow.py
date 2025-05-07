"""
Filename: s6_4_it_builds_the_map_that_keeps_track_of_flow.py
Purpose: Compiles all zone info into a persistent map for downstream logic.
Integrates activity detection with zone type classification.

Part of: Cycle 3 – Active Zone Management
Stanza 1 – The Mapping of Active Zones
"""

from typing import Dict, List
from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s6_3_it_names_the_zone_by_its_current_signs as zone_classifier
)


def build_zone_type_map(activity_log: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Given a log of active zones and their recent files,
    returns a dictionary mapping zone paths to their classified types.
    """
    if not activity_log:
        return {}

    return zone_classifier.assign_zone_types(activity_log)


if __name__ == "__main__":
    # Demo usage
    demo_input = {
        "zone_alpha": ["test_alpha.py"],
        "zone_beta": ["readme.md", "notes.txt"],
        "zone_gamma": ["fail_report.log"],
        "zone_delta": [],
    }

    zone_types = build_zone_type_map(demo_input)
    for zone, zone_type in zone_types.items():
        print(f"{zone}: {zone_type}")
