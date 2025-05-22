# s1_1_it_detects_a_returning_signal_signature.py

from typing import List, Dict
from collections import defaultdict

def detect_returning_signals(signal_log: List[str], memory_window: int = 100) -> Dict[str, int]:
    """
    Analyzes a list of signal IDs or hashes and returns those that have recurred more than once
    within the specified memory window.

    Args:
        signal_log (List[str]): A chronological list of signal identifiers.
        memory_window (int): The maximum number of most recent signals to consider.

    Returns:
        Dict[str, int]: A dictionary of signal IDs that appeared more than once within the window, with their counts.

    Example:
        >>> detect_returning_signals(["a", "b", "c", "a", "d", "b"])
        {'a': 2, 'b': 2}
    """
    recent_signals = signal_log[-memory_window:]
    counts = defaultdict(int)
    for sig in recent_signals:
        counts[sig] += 1

    return {sig: count for sig, count in counts.items() if count > 1}
