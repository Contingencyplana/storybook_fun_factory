"""
Filename: s3_1_it_detects_the_layer_misalignment.py

Detects when a recursion transition crosses a non-matching layer or zone.
Used to flag mismatches between expected and actual recursion layers.

Expected structure:
- Transition metadata includes both source and target layers
- Layers must follow a predefined adjacency or compatibility map
"""

from pathlib import Path
import json


# Example of allowed layer transitions
ALLOWED_LAYER_TRANSITIONS = {
    "layer_1": ["layer_2"],
    "layer_2": ["layer_1", "layer_3"],
    "layer_3": ["layer_2"]
}


def detect_layer_misalignment(metadata_path: Path) -> bool:
    """
    Detects if a transition crosses incompatible recursion layers.

    Args:
        metadata_path (Path): Path to the JSON file containing transition metadata.
            Expected keys: 'source_layer', 'target_layer'

    Returns:
        bool: True if misalignment detected, False otherwise.

    Example:
        >>> detect_layer_misalignment(Path("transition.json"))
        True
    """
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")

    with open(metadata_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    source = data.get("source_layer")
    target = data.get("target_layer")

    if source not in ALLOWED_LAYER_TRANSITIONS:
        return True  # Source unknown, treat as misalignment

    return target not in ALLOWED_LAYER_TRANSITIONS[source]
