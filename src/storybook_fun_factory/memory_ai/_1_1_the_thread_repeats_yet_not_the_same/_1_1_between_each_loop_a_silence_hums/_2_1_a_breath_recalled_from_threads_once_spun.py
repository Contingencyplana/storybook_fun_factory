"""
_2_1_a_breath_recalled_from_threads_once_spun.py

Retrieves previously logged memory fragments—traces drawn from earlier
decisions and recursive contexts. This file supports selective recall
of memory events based on filters such as timestamp, component, or action.
"""

from pathlib import Path
from typing import List, Optional
import json
import datetime

# Memory trace directory and file (shared with _1_1)
TRACE_DIR = Path.cwd() / "memory_ai" / "memory_chain" / "trace_logs"
TRACE_FILE = TRACE_DIR / "recursion_signatures.json"

# Ensure the directory exists
TRACE_DIR.mkdir(parents=True, exist_ok=True)

def load_memory_traces() -> List[dict]:
    """Load all memory trace entries from the log file."""
    if TRACE_FILE.exists():
        with open(TRACE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def filter_traces(
    component: Optional[str] = None,
    action: Optional[str] = None,
    since: Optional[str] = None
) -> List[dict]:
    """
    Filter memory traces by component, action, and timestamp threshold.
    - `since` should be an ISO 8601 timestamp string.
    """
    traces = load_memory_traces()
    results = []

    for trace in traces:
        if component and trace.get("component") != component:
            continue
        if action and trace.get("action") != action:
            continue
        if since:
            try:
                cutoff = datetime.datetime.fromisoformat(since)
                timestamp = datetime.datetime.fromisoformat(trace.get("timestamp", "1970-01-01T00:00:00"))
                if timestamp < cutoff:
                    continue
            except ValueError:
                continue
        results.append(trace)

    return results

# Example usage
if __name__ == "__main__":
    recalled = filter_traces(
        component="memory_ai",
        action="begin_layer_5_cycle",
        since="2025-04-01T00:00:00"
    )

    if not recalled:
        print("🧠 No matching memory fragments found.")
    else:
        print(f"🔎 Found {len(recalled)} matching memory fragments:")
        for r in recalled:
            print(f"• {r.get('action')} @ {r.get('timestamp')}")
