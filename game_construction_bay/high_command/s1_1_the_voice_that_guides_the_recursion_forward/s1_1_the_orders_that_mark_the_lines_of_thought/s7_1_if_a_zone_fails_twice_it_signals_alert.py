"""
Filename: s7_1_if_a_zone_fails_twice_it_signals_alert.py

Evaluates the Zone Map to detect zones that have failed more than once.
Flags such zones for review, generating alert records to be used for recursive escalation or intervention.

Failure is determined based on historical entries in the Zone Map under the 'failing' classification,
tracking repeated appearances over time or recurrent `.fail` indicators.

This function grants the Factory early warning capability—
not merely reacting to failure, but recognizing decay in progress.
"""

from typing import Dict, List

def flag_repeated_failures(zone_history: Dict[str, List[str]]) -> List[str]:
    """
    Examines historical zone classifications to identify zones
    that have been marked as 'failing' more than once.

    Parameters:
        zone_history (dict): A dictionary where keys are zone paths,
                             and values are lists of classification strings over time.

    Returns:
        List[str]: A list of zone paths that have failed more than once.
    """
    flagged_zones = []

    for zone, history in zone_history.items():
        fail_count = history.count('failing')
        if fail_count >= 2:
            flagged_zones.append(zone)

    return flagged_zones


# Example usage:
if __name__ == "__main__":
    # Mock zone history data structure
    example_history = {
        "game_construction_bay/visualizer/flowlines_of_logic": ["creative", "failing", "failing"],
        "game_construction_bay/filename_ai/": ["testing", "creative", "creative"],
        "game_construction_bay/dream_journal/": ["failing", "testing", "failing"],
    }

    alerts = flag_repeated_failures(example_history)
    for zone in alerts:
        print(f"⚠️ Alert: Zone '{zone}' has failed multiple times.")
