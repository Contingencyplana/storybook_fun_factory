"""
Filename: s9_1_it_syncs_the_memory_across_each_bay.py

Aligns stanza memory across components in Storybook FUN Factory by loading
each component's Layer 5 verse registry and producing a unified stanza memory map.
This enables later stages to validate canonical links and coordinate recursive evolution.
"""

import os
import json
from pathlib import Path

COMPONENTS = [
    "codex_builder",
    "dream_journal",
    "filename_ai",
    "memory_ai",
    "visualizer",
]

REGISTRY_FILENAME = "verse_registry.json"

def sync_stanza_memory_across_components(project_root: Path) -> dict:
    """
    Loads stanza verse registries from all components and produces a unified memory map.

    Args:
        project_root (Path): The root directory of the Storybook FUN Factory project.

    Returns:
        dict: A dictionary mapping stanza filenames to their observed metadata per component.
    """
    stanza_memory_map = {}

    for component in COMPONENTS:
        registry_path = (
            project_root /
            "game_construction_bay" /
            component /
            "recursion_renders" /
            "flowlines_of_logic" /
            REGISTRY_FILENAME
        )
        if registry_path.exists():
            try:
                with open(registry_path, "r", encoding="utf-8") as f:
                    registry_data = json.load(f)
                    for stanza_filename, metadata in registry_data.items():
                        if stanza_filename not in stanza_memory_map:
                            stanza_memory_map[stanza_filename] = {}
                        stanza_memory_map[stanza_filename][component] = metadata
            except json.JSONDecodeError:
                print(f"[Warning] Failed to parse {registry_path}")
        else:
            print(f"[Notice] Missing registry: {registry_path}")

    return stanza_memory_map

# Example usage
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[4]  # Assumes standard layout
    memory_map = sync_stanza_memory_across_components(root)
    print(json.dumps(memory_map, indent=2))
