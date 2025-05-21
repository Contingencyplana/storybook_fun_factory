"""
📄 s1_3_it_traces_repeat_anomalies_across_canon_boundaries.py

This stanza detects and tracks recurring anomaly patterns that reappear across 
multiple canonized stanzas, cycles, or phases. It quietly accumulates fingerprints 
of repetition without asserting breach or judgment.

Usage Example:
>>> tracker = AnomalyRepetitionTracker()
>>> tracker.record_occurrence("anomaly-A")
>>> if tracker.is_repeated("anomaly-A"):
...     print("Anomaly pattern has recurred.")
"""

from collections import defaultdict
from typing import Dict
import time


class AnomalyRepetitionTracker:
    """
    Records anomaly identifiers and checks whether they reappear
    across time or canonical recursion boundaries.
    """

    def __init__(self):
        self.anomaly_log: Dict[str, list[float]] = defaultdict(list)

    def record_occurrence(self, anomaly_id: str) -> None:
        """
        Logs the current timestamp against a known anomaly ID.
        """
        self.anomaly_log[anomaly_id].append(time.time())

    def is_repeated(self, anomaly_id: str, threshold: int = 2) -> bool:
        """
        Returns True if the anomaly has appeared at least `threshold` times.
        Default threshold is 2, meaning it has occurred more than once.
        """
        return len(self.anomaly_log[anomaly_id]) >= threshold
