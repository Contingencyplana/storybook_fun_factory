"""
Filename: s7_2_if_a_zone_sleeps_it_prods_for_motion.py

Identifies zones that have shown no recent activity over a specified time threshold.
Flags these zones as "sleeping" and recommends reactivation actions.

This function enables the assistant to detect developmental stagnation—
not by failure, but by absence—and gently nudge progress forward.

It is the Factory's memory of momentum gone still.
"""

from typing import Dict, List
from datetime import datetime, timedelta, timezone

def detect_stale_zones(
    last_modified_map: Dict[str, str], 
    threshold_days: int = 7
) -> List[str]:
    """
    Identifies zones that haven't been modified in more than `threshold_days`.

    Parameters:
        last_modified_map (dict): Maps zone paths to ISO 8601 UTC timestamp strings.
        threshold_days (int): How many days of inactivity qualifies as "sleeping".

    Returns:
        List[str]: List of zone paths considered stale.
    """
    stale_zones = []
    now = datetime.now(timezone.utc)
    threshold = timedelta(days=threshold_days)

    for zone, iso_timestamp in last_modified_map.items():
        try:
            modified_time = datetime.fromisoformat(iso_timestamp)
            if now - modified_time > threshold:
                stale_zones.append(zone)
        except ValueError:
            # Invalid timestamp format — optionally log or skip
            continue

    return stale_zones


# Example usage
if __name__ == "__main__":
    example_map = {
        "game_construction_bay/filename_ai/": "2025-04-30T14:00:00",
        "game_construction_bay/dream_journal/": "2025-05-09T02:00:00",
        "game_construction_bay/memory_ai/": "2025-04-25T09:45:00",
    }

    stale = detect_stale_zones(example_map, threshold_days=10)
    for zone in stale:
        print(f"🛌 Prodding dormant zone: {zone}")
