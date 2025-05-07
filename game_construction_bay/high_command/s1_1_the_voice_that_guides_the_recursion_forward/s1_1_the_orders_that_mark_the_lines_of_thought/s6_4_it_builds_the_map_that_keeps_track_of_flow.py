"""
Filename: s6_4_it_builds_the_map_that_keeps_track_of_flow.py
Purpose: Compiles all zone information — recent activity, timestamps, and classifications —
into a persistent and queryable map used for downstream logic and assistant awareness.

Part of: Cycle 3 – Active Zone Management
Stanza 1 – The Mapping of Active Zones
"""

import json
from pathlib import Path
from typing import Dict, List

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s6_1_it_detects_the_zones_that_shift_and_turn as detector,
    s6_2_it_logs_each_zone_and_marks_the_time as logger,
    s6_3_it_names_the_zone_by_its_current_signs as classifier,
)


def build_zone_map(root_dir: Path, output_path: Path) -> Dict[str, Dict[str, str]]:
    """
    Constructs a zone map: a dictionary where each zone path maps to a dictionary
    with:
        • 'type': the classified zone type
        • 'last_modified': last modified timestamp string
        • 'files': comma-separated list of recently active files

    The result is saved as a JSON file to `output_path`.
    """
    active_zones = detector.scan_for_active_zones(root_dir)
    timestamps = logger.log_zone_timestamps(root_dir)
    types = classifier.assign_zone_types(active_zones)

    zone_map = {}
    for zone in active_zones:
        zone_map[zone] = {
            "type": types.get(zone, "unknown"),
            "last_modified": timestamps.get(zone, "unknown"),
            "files": ", ".join(active_zones[zone])
        }

    output_path.write_text(json.dumps(zone_map, indent=2))
    return zone_map


def print_zone_map(zone_map: Dict[str, Dict[str, str]]):
    """Prints the zone map in a readable format."""
    print("\n🗺️ Zone Awareness Map:\n")
    for zone, data in zone_map.items():
        print(f"📁 {zone}/")
        print(f"    ├ Type: {data['type']}")
        print(f"    ├ Last Modified: {data['last_modified']}")
        print(f"    └ Files: {data['files']}")
        print()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]  # Adjust as needed
    output_file = project_root / "zone_map.json"

    zone_map = build_zone_map(project_root, output_file)
    print_zone_map(zone_map)
