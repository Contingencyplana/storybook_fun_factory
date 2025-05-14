"""
Filename: s2_3_it_flags_the_name_when_identity_has_split.py

Identifies and logs canonical name misalignment or drift in recursive transitions.
Flags cases where an entity's identity is split, overwritten, or mismatched.
"""

from pathlib import Path
import json


def flag_identity_drift(name_trace_path: Path) -> bool:
    """
    Checks a name trace file for signs of identity divergence during recursion.

    Expected indicators of drift:
    - Mismatch between 'expected_name' and 'actual_name'
    - Presence of 'identity_conflict': true

    Args:
        name_trace_path (Path): Path to the trace file (JSON format)

    Returns:
        bool: True if identity has split or diverged; False if aligned

    Example:
        >>> flag_identity_drift(Path("logs/name_trace.json"))
        True
    """
    if not name_trace_path.exists():
        return False

    try:
        with open(name_trace_path, "r", encoding="utf-8") as f:
            trace = json.load(f)
    except (json.JSONDecodeError, IOError):
        return False

    expected = trace.get("expected_name")
    actual = trace.get("actual_name")
    conflict = trace.get("identity_conflict", False)

    return (expected != actual) or conflict is True
