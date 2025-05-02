"""
Filename: s1_2_a_mirrored_path_a_whispered_when.py

Encodes reflective time-awareness, enabling assistant systems to track
the “when” of remembered paths. Compares current event timestamps to
past memory entries to detect temporal patterns, delays, and cyclical triggers.
"""

from pathlib import Path
from datetime import datetime
import json

# Define where time-trace logs are stored
TIME_TRACE_DIR = Path.cwd() / "memory_ai" / "memory_chain" / "trace_logs"
TIME_TRACE_FILE = TIME_TRACE_DIR / "timestamp_traces.json"

# Ensure the directory exists
TIME_TRACE_DIR.mkdir(parents=True, exist_ok=True)

def store_timestamp_event(event_key: str, timestamp: str = None) -> None:
    """Stores the current or given timestamp for a specific memory event key."""
    if timestamp is None:
        timestamp = datetime.now().isoformat()

    existing_data = load_time_traces()
    existing_data.setdefault(event_key, []).append(timestamp)

    with open(TIME_TRACE_FILE, "w") as f:
        json.dump(existing_data, f, indent=2)

def load_time_traces() -> dict:
    """Loads all previously recorded timestamp events."""
    if TIME_TRACE_FILE.exists():
        with open(TIME_TRACE_FILE, "r") as f:
            return json.load(f)
    return {}

def time_since_last_event(event_key: str) -> float:
    """
    Returns the number of seconds since the last recorded timestamp
    for the given event_key. Returns -1 if no prior timestamp exists.
    """
    traces = load_time_traces()
    timestamps = traces.get(event_key, [])

    if not timestamps:
        return -1

    last_timestamp = datetime.fromisoformat(timestamps[-1])
    now = datetime.now()
    delta = now - last_timestamp
    return delta.total_seconds()

# Example usage
if __name__ == "__main__":
    event = "memory_ai.trace_intervals.first_contact"

    # Log the current timestamp for this event
    store_timestamp_event(event)

    # Optionally check time since last log
    elapsed = time_since_last_event(event)
    if elapsed == -1:
        print("🕰️ First time logging this memory event.")
    else:
        print(f"⏳ {elapsed:.2f} seconds since last occurrence of this event.")
