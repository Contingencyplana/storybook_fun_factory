"""
Filename: s9_3_it_prepares_the_paths_for_crossing_safe.py

Identifies which stanza lines are ready for synchronized recursion.
Marks as ready if stanza exists in 2+ components and passes canon confirmation.
"""

from pathlib import Path
import json

def mark_ready_stanza_paths(confirmed_canon_map: dict, min_components: int = 2) -> dict:
    """
    Filters stanza lines that are ready for cross-component recursion.

    A stanza is marked ready if it appears in at least `min_components`.

    Args:
        confirmed_canon_map (dict): Canon-confirmed stanza memory.
        min_components (int): Minimum number of components required for readiness.

    Returns:
        dict: Mapping of ready stanza lines to their participating components.
    """
    ready = {}
    for stanza_file, component_map in confirmed_canon_map.items():
        if len(component_map) >= min_components:
            ready[stanza_file] = {
                "components": list(component_map.keys()),
                "status": "ready"
            }
    return ready

def save_ready_paths(ready_map: dict, output_path: Path) -> None:
    """
    Saves the ready stanza path list to a JSON file.

    Args:
        ready_map (dict): Map of ready stanza lines with components.
        output_path (Path): Path to save the output JSON.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ready_map, f, indent=2)

# Example usage
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[4]
    input_path = root / "game_construction_bay" / "high_command" / "tmp" / "confirmed_canon.json"
    output_path = root / "game_construction_bay" / "high_command" / "tmp" / "ready_crossings.json"

    if input_path.exists():
        with open(input_path, "r", encoding="utf-8") as f:
            confirmed = json.load(f)
        ready = mark_ready_stanza_paths(confirmed)
        save_ready_paths(ready, output_path)
    else:
        print(f"[Error] Missing input: {input_path}")
