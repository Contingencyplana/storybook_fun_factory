"""
Filename: s8_1_it_detects_each_depth_and_marks_the_place.py

Purpose:
Recursively scans each registered component’s Layer 5 directory path and reports which stanza lines are present.
Outputs a dictionary mapping stanza file presence per component, suitable for use by cross-system coordination logic.

Poetic Role:
The Gate That Knows Each Line Beneath – Line 1
"""

import os
from pathlib import Path

COMPONENTS = [
    "codex_builder",
    "dream_journal",
    "filename_ai",
    "memory_ai",
    "visualizer"
]

def detect_layer5_stanza_files(project_root: Path) -> dict:
    """
    Scans each component’s Layer 5 directory to identify stanza files.

    Args:
        project_root (Path): Root directory of the project

    Returns:
        dict: Mapping of component → list of stanza file paths (relative to root)
    """
    results = {}

    for component in COMPONENTS:
        stanza_dir = project_root / "game_construction_bay" / component
        matches = []

        for root, dirs, files in os.walk(stanza_dir):
            for file in files:
                if file.startswith("s") and file.endswith(".py"):
                    file_path = Path(root) / file
                    matches.append(file_path.relative_to(project_root))

        results[component] = sorted(str(p) for p in matches)

    return results

# Example usage
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    print(detect_layer5_stanza_files(root))
