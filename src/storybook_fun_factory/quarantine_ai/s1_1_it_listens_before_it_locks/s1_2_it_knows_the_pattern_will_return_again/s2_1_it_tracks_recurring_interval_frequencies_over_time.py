"""
📄 s2_1_it_tracks_recurring_interval_frequencies_over_time.py
-------------------------------------------------------------
Analyzes the time intervals between recurring signal echoes and logs frequency patterns.

Part of the stanza: The Pattern Hidden in the Repeats
"""

import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def compute_intervals(signal_log_file):
    """
    Computes the time intervals (in seconds) between recurring signals.

    Parameters:
    - signal_log_file (str or Path): Path to a JSONL file where each line is a {"timestamp", "signal"} dict.

    Returns:
    - Dict[str, List[float]]: Mapping of signal to list of time intervals (in seconds) between appearances.
    """
    path = Path(signal_log_file)
    if not path.exists():
        return {}

    signal_times = defaultdict(list)

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                ts = datetime.fromisoformat(entry["timestamp"])
                signal = entry["signal"]
                signal_times[signal].append(ts)
            except (json.JSONDecodeError, KeyError, ValueError):
                continue

    intervals = {}
    for signal, timestamps in signal_times.items():
        timestamps.sort()
        deltas = [(t2 - t1).total_seconds() for t1, t2 in zip(timestamps, timestamps[1:])]
        if deltas:
            intervals[signal] = deltas

    return intervals
