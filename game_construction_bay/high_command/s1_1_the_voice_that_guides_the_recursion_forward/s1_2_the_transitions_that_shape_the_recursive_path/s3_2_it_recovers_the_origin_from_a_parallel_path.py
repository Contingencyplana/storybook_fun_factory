"""
Filename: s3_2_it_recovers_the_origin_from_a_parallel_path.py

Attempts to reconstruct the origin point of a recursion transition that 
has veered into a parallel timeline or divergent layer.

Expected structure:
- Transition metadata includes both initial and current trace fragments
- Recovery attempts are made using fallback mapping logic and origin signatures
"""

from pathlib import Path
import json


def recover_origin_from_parallel_path(metadata_path: Path) -> str:
    """
    Reconstructs the original origin of a recursion transition using provided metadata.

    Args:
        metadata_path (Path): Path to a JSON file with keys:
            - 'initial_trace' (str): presumed origin trace
            - 'current_position' (str): current location or corrupted marker
            - 'recovery_map' (dict): known corrections from broken to valid origins

    Returns:
        str: Recovered origin trace if successful, or 'unknown_origin' if recovery fails.

    Example:
        >>> recover_origin_from_parallel_path(Path("parallel_trace.json"))
        'layer_2:start_sequence'
    """
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")

    with open(metadata_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    current = data.get("current_position")
    fallback_map = data.get("recovery_map", {})

    return fallback_map.get(current, "unknown_origin")
