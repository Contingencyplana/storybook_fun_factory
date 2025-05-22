"""
📄 s1_4_it_flags_any_signal_that_returns_in_pattern.py
------------------------------------------------------
Detects and flags signals that recur frequently enough to suggest an underlying pattern.
Used to pre-flag potentially recursive behavior in anomaly traces.

Part of the stanza: The Signal That Returned Again
"""

import json
from collections import defaultdict
from pathlib import Path

def flag_repeating_signals(signal_log_file, threshold=2):
    """
    Flags all signals that appear equal to or above the threshold.

    Parameters:
    - signal_log_file (str or Path): Path to a JSONL file (one JSON object per line) containing signal entries.
    - threshold (int): Minimum number of occurrences to flag a signal.

    Returns:
    - List[dict]: Signals (as dicts) that met or exceeded the threshold.
    """
    signal_counts = defaultdict(int)
    signal_instances = defaultdict(list)

    path = Path(signal_log_file)
    if not path.exists():
        return []

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                sig_str = json.dumps(entry, sort_keys=True)
                signal_counts[sig_str] += 1
                signal_instances[sig_str].append(entry)
            except json.JSONDecodeError:
                continue

    return [
        signal_instances[sig][0]
        for sig, count in signal_counts.items()
        if count >= threshold
    ]
