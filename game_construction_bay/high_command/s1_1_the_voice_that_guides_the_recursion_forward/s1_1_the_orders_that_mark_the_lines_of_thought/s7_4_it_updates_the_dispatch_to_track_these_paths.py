"""
Filename: s7_4_it_updates_the_dispatch_to_track_these_paths.py

Feeds updated zone status into the Dispatch Logic system.

This function takes a classified Zone Map and determines whether
any dispatch targets should change in priority or scope based on recent heat.

It acts as a feedback mechanism — aligning strategic awareness with tactical output.

It is the Factory’s instinct to turn attention where it’s most needed.
"""

from typing import Dict, List

def update_dispatch_targets(
    classified_zone_map: Dict[str, str],
    current_dispatch_targets: List[str]
) -> List[str]:
    """
    Updates dispatch targets based on the classified zone map.

    Parameters:
        classified_zone_map (dict): Maps zone paths to classifications (e.g., 'creative', 'failing', 'stalled').
        current_dispatch_targets (list): Current list of dispatch target paths.

    Returns:
        list: Updated list of dispatch targets, sorted with priority zones first.
    """
    priority_order = ['failing', 'testing', 'creative', 'stalled']
    bucketed = {status: [] for status in priority_order}

    for zone, status in classified_zone_map.items():
        if status in bucketed:
            bucketed[status].append(zone)

    # Prioritize by classification and append any previously active targets not seen
    updated_targets = []
    for status in priority_order:
        updated_targets.extend(bucketed[status])

    unseen = [z for z in current_dispatch_targets if z not in updated_targets]
    updated_targets.extend(unseen)

    return updated_targets


# Example usage
if __name__ == "__main__":
    classified_map = {
        "game_construction_bay/filename_ai/": "creative",
        "game_construction_bay/visualizer/": "failing",
        "game_construction_bay/dream_journal/": "testing",
        "game_construction_bay/codex_builder/": "stalled"
    }

    active_targets = ["game_construction_bay/memory_ai/"]

    new_dispatch = update_dispatch_targets(classified_map, active_targets)

    for target in new_dispatch:
        print(f"🎯 Dispatch: {target}")
