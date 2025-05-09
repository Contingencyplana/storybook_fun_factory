"""
Filename: s7_3_if_a_zone_burns_hot_it_spreads_attention.py

Detects zones that show signs of rapidly increasing activity.
These "hot zones" are where creation accelerates—often requiring additional
attention, review, or AI/player focus to prevent overload, burnout, or neglect of adjacent zones.

A zone is considered hot if it has shown more than a defined threshold of modifications
within a recent time window.

This function brings awareness to the intensity of recursion—
ensuring that fire does not spread uncontained.
"""

from typing import Dict, List
from datetime import datetime, timedelta, timezone

def detect_hot_zones(
    zone_activity_log: Dict[str, List[str]],
    recent_window_minutes: int = 60,
    activity_threshold: int = 3
) -> List[str]:
    """
    Identifies zones with high-frequency activity in a recent window.

    Parameters:
        zone_activity_log (dict): Maps zone paths to lists of ISO UTC timestamps (str).
        recent_window_minutes (int): Time window in minutes for defining "recent" activity.
        activity_threshold (int): Number of recent activity events required to flag a zone as hot.

    Returns:
        List[str]: List of hot zone paths.
    """
    hot_zones = []
    now = datetime.now(timezone.utc)
    window = timedelta(minutes=recent_window_minutes)

    for zone, timestamp_list in zone_activity_log.items():
        recent_events = 0
        for iso in timestamp_list:
            try:
                dt = datetime.fromisoformat(iso)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if now - dt <= window:
                    recent_events += 1
            except ValueError:
                continue

        if recent_events >= activity_threshold:
            hot_zones.append(zone)

    return hot_zones


# Example usage
if __name__ == "__main__":
    log = {
        "zone_a": [
            "2025-05-09T00:00:00",
            "2025-05-09T00:05:00",
            "2025-05-09T00:15:00",
        ],
        "zone_b": [
            "2025-05-08T20:00:00",
            "2025-05-08T22:00:00",
        ],
        "zone_c": [
            "2025-05-09T00:01:00",
            "2025-05-09T00:02:00",
            "2025-05-09T00:03:00",
            "2025-05-09T00:04:00",
        ],
    }

    hot = detect_hot_zones(log, recent_window_minutes=30, activity_threshold=3)
    for z in hot:
        print(f"🔥 Hot zone detected: {z}")
