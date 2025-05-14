"""
Filename: s8_3_it_tracks_the_names_and_maps_the_form.py

Purpose:
Builds a registry of stanza files organized by filename, component, and stanza ID.
Reads from the trace file created by s8_2 and organizes cross-system verse metadata.

Poetic Role:
The Gate That Knows Each Line Beneath – Line 3
"""

import json
from pathlib import Path

TRACE_FILENAME = "layer5_trace.json"

def build_verse_registry(trace_dir: Path) -> dict:
    """
    Builds a registry of stanza lines from the trace JSON.

    Args:
        trace_dir (Path): Directory containing the trace file

    Returns:
        dict: Registry mapping stanza filename → {component, path}
    """
    trace_path = trace_dir / TRACE_FILENAME
    if not trace_path.exists():
        raise FileNotFoundError(f"Trace file not found at: {trace_path}")

    with open(trace_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    registry = {}
    for component, paths in data.items():
        for path in paths:
            filename = Path(path).name
            registry[filename] = {
                "component": component,
                "path": path
            }

    return registry

# Example usage
if __name__ == "__main__":
    registry = build_verse_registry(Path.cwd())
    print(json.dumps(registry, indent=2))
