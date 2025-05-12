"""
Filename: s2_2_it_restores_the_memory_from_a_partial_state.py

Recovers memory context from incomplete or degraded recursive transitions.
Searches for recovery markers and restores key memory values.
"""

from pathlib import Path
import json


def restore_partial_memory(snapshot_path: Path) -> dict:
    """
    Attempts to recover memory from a partial transition state.

    Validates that:
    - Snapshot file exists
    - It contains "memory_state" with non-null, non-empty data
    - If corrupted or missing, returns empty dict as fallback

    Args:
        snapshot_path (Path): Path to the JSON snapshot file

    Returns:
        dict: Recovered memory context, or empty dict if unrecoverable

    Example:
        >>> restore_partial_memory(Path("logs/memory_snapshot.json"))
        {'player_id': 42, 'cycle': 'filename_ai', 'loop_index': 3}
    """
    if not snapshot_path.exists():
        return {}

    try:
        with open(snapshot_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        memory = data.get("memory_state")
        if isinstance(memory, dict) and memory:
            return memory
    except (json.JSONDecodeError, IOError):
        pass

    return {}
