"""
Filename: s2_1_when_a_component_falls_another_rises.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Second Stanza, Line 1 – Detecting stagnation and triggering strategic pivot)

This module reviews recent stanza activity.
If the most recent line is too old, it recommends switching components.
"""

from pathlib import Path
from datetime import datetime, timedelta, UTC
import json
import random

# 🔖 Shared state files
ACTIVE_FRONT_PATH = Path(__file__).parent / "active_front.json"
STANZA_TRACE_PATH = Path(__file__).parent / "stanza_path_log.json"

def detect_and_pivot_if_stalled(timeout_seconds=3600):
    """
    Checks if the most recent stanza log is stale. If so, returns a pivot recommendation.

    Returns:
        dict: Either a no-op signal or pivot suggestion
    """
    if not STANZA_TRACE_PATH.exists():
        return {"status": "no_data", "reason": "no_trace_file"}

    try:
        with STANZA_TRACE_PATH.open("r", encoding="utf-8") as f:
            trace_log = json.load(f)
    except json.JSONDecodeError:
        return {"status": "no_data", "reason": "trace_file_corrupt"}

    if not trace_log:
        return {"status": "no_data", "reason": "trace_log_empty"}

    latest = trace_log[-1]
    timestamp_str = latest.get("timestamp", "")
    try:
        last_time = datetime.fromisoformat(timestamp_str)
    except ValueError:
        return {"status": "no_data", "reason": "bad_timestamp"}

    now = datetime.now(UTC)
    delta = now - last_time.replace(tzinfo=UTC)

    if delta.total_seconds() > timeout_seconds:
        prev_component = latest.get("component", "unknown")
        possible_components = [
            "codex_builder", "dream_journal", "filename_ai", "memory_ai", "visualizer"
        ]
        try:
            possible_components.remove(prev_component)
        except ValueError:
            pass

        next_component = random.choice(possible_components)

        return {
            "status": "pivot",
            "previous_component": prev_component,
            "suggested_component": next_component,
            "reason": f"Last activity was {int(delta.total_seconds())} seconds ago."
        }

    return {"status": "continue", "last_active": latest}
