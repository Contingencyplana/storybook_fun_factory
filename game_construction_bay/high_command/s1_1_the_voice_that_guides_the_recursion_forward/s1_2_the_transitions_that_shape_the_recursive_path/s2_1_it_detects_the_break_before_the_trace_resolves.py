"""
Filename: s2_1_it_detects_the_break_before_the_trace_resolves.py

Detects interruptions or mid-transition collapse before canonical linkage occurs.
Acts as an early warning system for recursive handoffs that do not complete their trace.
"""

from pathlib import Path


def detect_mid_transition_break(log_path: Path) -> bool:
    """
    Scans a recursive transition log for signs of premature interruption.
    Returns True if break detected before canonical trace completes; otherwise False.

    Expected signals:
    - "HANDOFF_INITIATED"
    - No subsequent "CANONICAL_TRACE_LINKED"
    - Or presence of "HANDOFF_ABORTED"

    Args:
        log_path (Path): Path to the transition log file.

    Returns:
        bool: True if break detected before trace resolution; False if normal.

    Example:
        >>> detect_mid_transition_break(Path("logs/transition_log.txt"))
        True
    """
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    initiated = any("HANDOFF_INITIATED" in line for line in lines)
    linked = any("CANONICAL_TRACE_LINKED" in line for line in lines)
    aborted = any("HANDOFF_ABORTED" in line for line in lines)

    return initiated and (not linked or aborted)
