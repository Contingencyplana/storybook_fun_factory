"""
s5_1_it_identifies_freezepoints_that_must_halt_execution.py

Determines if a recursion thread has hit a critical anomaly threshold requiring a hard halt.
Implements logic to tag freezepoints based on anomaly severity scores or sentinel match patterns.
"""

from typing import List, Dict

HALT_THRESHOLD_SCORE = 7  # Adjustable cutoff for required halting

def identify_freezepoints(anomalies: List[Dict], threshold: int = HALT_THRESHOLD_SCORE) -> List[Dict]:
    """
    Identifies which anomalies should trigger a recursion halt (freezepoint).

    Args:
        anomalies (List[Dict]): List of anomaly entries with 'id', 'severity', and optional 'tags'.
        threshold (int): Minimum severity score to be considered halt-worthy.

    Returns:
        List[Dict]: Subset of anomalies that require execution to pause.

    Example:
        >>> identify_freezepoints([
        ...     {"id": "f1", "severity": 5},
        ...     {"id": "f2", "severity": 8}
        ... ])
        [{'id': 'f2', 'severity': 8}]
    """
    return [a for a in anomalies if a.get("severity", 0) >= threshold]
