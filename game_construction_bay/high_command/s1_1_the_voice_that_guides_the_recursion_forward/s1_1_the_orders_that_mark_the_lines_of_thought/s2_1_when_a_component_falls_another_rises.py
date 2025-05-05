"""
Filename: s2_1_when_a_component_falls_another_rises.py

📜 Second Stanza, Line 1 of Genesis Command
(A responsive trigger that pivots the active front when a component becomes dormant)

Purpose:
Automatically detects when the current active component appears dormant or stagnant,
and intelligently pivots the focus to a new viable component or stanza path.
This maintains project momentum and simulates assistant-guided recursive flexibility.

Plays a key role in High Command's autonomous decision support.
"""

import json
from pathlib import Path
from datetime import datetime, UTC

# Shared memory locations
ACTIVE_FRONT_PATH = Path(__file__).parent / "active_front.json"
STANZA_TRACE_PATH = Path(__file__).parent / "stanza_path_log.json"

# Configuration: maximum allowed seconds of stagnation before auto-pivot
DEFAULT_TIMEOUT_SECONDS = 7200  # 2 hours


def detect_and_pivot_if_stalled(timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS):
    """
    Checks whether the current active front has been idle too long,
    and if so, suggests or initiates a shift to a new stanza/component.

    Returns:
        dict: Details of the pivot decision (if any)
    """
    if not ACTIVE_FRONT_PATH.exists() or not STANZA_TRACE_PATH.exists():
        return {"status": "no_data", "reason": "Missing front or trace log"}

    # Load trace log
    with STANZA_TRACE_PATH.open("r", encoding="utf-8") as f:
        entries = json.load(f)

    if not entries:
        return {"status": "no_data", "reason": "Trace log is empty"}

    # Sort and examine the most recent entry
    latest_entry = sorted(entries, key=lambda e: e["timestamp"], reverse=True)[0]
    last_time = datetime.fromisoformat(latest_entry["timestamp"])
    now = datetime.now(UTC)
    elapsed_seconds = (now - last_time).total_seconds()

    if elapsed_seconds < timeout_seconds:
        return {"status": "active", "reason": "Recent activity", "seconds_idle": elapsed_seconds}

    # Timeout exceeded: suggest pivot
    previous_component = latest_entry["component"]
    pivot_to = _suggest_next_component(previous_component)

    return {
        "status": "pivot",
        "reason": "Timeout exceeded",
        "seconds_idle": elapsed_seconds,
        "previous_component": previous_component,
        "suggested_component": pivot_to,
    }


def _suggest_next_component(current: str) -> str:
    """
    Suggests another component to pivot to if the current is stalled.
    Uses simple alphabetical rotation for now.
    """
    components = ["codex_builder", "dream_journal", "filename_ai", "memory_ai", "visualizer"]
    if current not in components:
        return components[0]
    index = components.index(current)
    return components[(index + 1) % len(components)]


# Optional CLI diagnostic
if __name__ == "__main__":
    result = detect_and_pivot_if_stalled()
    print(json.dumps(result, indent=2))
