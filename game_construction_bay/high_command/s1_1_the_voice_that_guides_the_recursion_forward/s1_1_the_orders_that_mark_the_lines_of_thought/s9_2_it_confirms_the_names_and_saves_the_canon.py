"""
Filename: s9_2_it_confirms_the_names_and_saves_the_canon.py

Validates stanza line names against GDJ anchors and canonical naming conventions.
Saves a filtered version of the stanza memory map containing only confirmed entries.
"""

import os
import json
from pathlib import Path

def confirm_canonical_stanza_names(memory_map: dict, valid_names: set) -> dict:
    """
    Confirms stanza line names against canonical naming rules.

    Args:
        memory_map (dict): Raw stanza memory map keyed by filename.
        valid_names (set): Set of valid stanza filenames (as determined by canon).

    Returns:
        dict: Filtered memory map with only confirmed stanza lines.
    """
    confirmed = {}
    for filename, component_map in memory_map.items():
        if filename in valid_names:
            confirmed[filename] = component_map
        else:
            print(f"[Warning] Filename not in canon: {filename}")
    return confirmed

def save_confirmed_canon(confirmed_map: dict, output_path: Path) -> None:
    """
    Saves the confirmed stanza registry to a new JSON file.

    Args:
        confirmed_map (dict): Canon-confirmed stanza memory.
        output_path (Path): Where to save the file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(confirmed_map, f, indent=2)

# Example usage
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[4]
    registry_path = root / "game_construction_bay" / "high_command" / "tmp" / "confirmed_canon.json"

    # Example placeholders
    from s9_1_it_syncs_the_memory_across_each_bay import sync_stanza_memory_across_components
    stanza_memory = sync_stanza_memory_across_components(root)

    # Simulate a valid name list (in reality this should come from GDJ anchor)
    valid_stanza_names = set(stanza_memory.keys())  # Accept all for now
    confirmed = confirm_canonical_stanza_names(stanza_memory, valid_stanza_names)
    save_confirmed_canon(confirmed, registry_path)
