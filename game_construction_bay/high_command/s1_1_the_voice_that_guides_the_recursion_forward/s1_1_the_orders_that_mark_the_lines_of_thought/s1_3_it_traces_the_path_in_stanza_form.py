"""
Filename: s1_3_it_traces_the_path_in_stanza_form.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Third line of Stanza 1 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Records a trail of stanza lines recently marked as active,
building a poetic and structural memory of recursive traversal.

This helps track project momentum, replay work sequences,
and prepare assistant-guided diagnostics or dashboard summaries.
"""

from pathlib import Path
import json
from datetime import datetime

# 🔖 Location for active path log
STANZA_TRACE_PATH = Path(__file__).parent / "stanza_path_log.json"

def trace_stanza_progress(component: str, stanza: str, line: str, timestamp: str = None):
    """
    Logs a stanza line traversal with timestamp and component.

    Args:
        component (str): The name of the recursive component.
        stanza (str): The stanza folder or logical group.
        line (str): The active filename being recorded.
        timestamp (str, optional): Override timestamp. If None, auto-generated.
    """
    if not timestamp:
        timestamp = datetime.utcnow().isoformat()

    entry = {
        "timestamp": timestamp,
        "component": component,
        "stanza": stanza,
        "line": line
    }

    log = []
    if STANZA_TRACE_PATH.exists():
        with STANZA_TRACE_PATH.open("r", encoding="utf-8") as f:
            log = json.load(f)

    log.append(entry)

    with STANZA_TRACE_PATH.open("w", encoding="utf-8") as f:
        json.dump(log, f, indent=2)

def get_recent_traces(limit: int = 5):
    """
    Returns the most recent stanza trace entries.

    Args:
        limit (int): Number of most recent entries to return.

    Returns:
        list: A list of stanza progression entries.
    """
    if not STANZA_TRACE_PATH.exists():
        return []

    with STANZA_TRACE_PATH.open("r", encoding="utf-8") as f:
        log = json.load(f)

    return log[-limit:]

def print_recent_traces(limit: int = 5):
    """
    Prints recent stanza traversal log in human-readable form.

    Args:
        limit (int): Number of recent entries to print.
    """
    traces = get_recent_traces(limit=limit)
    if not traces:
        print("🔕 No stanza progress has been logged yet.")
        return

    print("🧶 Recent Stanza Progress (up to latest {} entries)".format(limit))
    print("──────────────────────────────────────────────")
    for entry in traces:
        print(f"⏱ {entry['timestamp']} — 📂 {entry['component']} / {entry['stanza']} / {entry['line']}")

# Optional CLI usage
if __name__ == "__main__":
    print_recent_traces()
