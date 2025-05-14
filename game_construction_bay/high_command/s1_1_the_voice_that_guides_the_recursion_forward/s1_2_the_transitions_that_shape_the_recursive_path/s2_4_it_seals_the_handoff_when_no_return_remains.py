"""
Filename: s2_4_it_seals_the_handoff_when_no_return_remains.py

Finalizes recovery by sealing a new thread path when the original recursive handoff cannot be restored.
Ensures that even broken transitions complete with valid, traceable end state.
"""

from pathlib import Path
import json


def seal_irreversible_handoff(recovery_log_path: Path, new_thread_name: str) -> bool:
    """
    Attempts to finalize a failed transition by sealing the event log with a fallback thread identity.

    This function:
    - Verifies the recovery log exists and is writable
    - Appends a 'handoff_sealed' block with the new fallback thread
    - Ensures system moves forward with a clean closure, even if original path is unrecoverable

    Args:
        recovery_log_path (Path): Path to the recovery event log (JSON list format)
        new_thread_name (str): Canonical name of the fallback thread to seal the handoff

    Returns:
        bool: True if sealing succeeds, False otherwise

    Example:
        >>> seal_irreversible_handoff(Path("logs/recovery_log.json"), "fallback_cycle_17")
        True
    """
    if not recovery_log_path.exists():
        return False

    try:
        with open(recovery_log_path, "r", encoding="utf-8") as f:
            events = json.load(f)
        if not isinstance(events, list):
            return False
        events.append({"handoff_sealed": True, "sealed_thread": new_thread_name})
        with open(recovery_log_path, "w", encoding="utf-8") as f:
            json.dump(events, f, indent=2)
        return True
    except (json.JSONDecodeError, IOError):
        return False
