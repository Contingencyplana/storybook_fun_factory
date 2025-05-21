"""
📄 s1_1_it_detects_the_first_anomalous_loop_signature.py

Detects the earliest sign of a recursive loop that deviates from expected pattern.
Part of the first cradle stanza in `quarantine_ai/`, this file listens quietly for 
early anomaly signatures and logs any deviation — without intervention.

It is designed to prepare the system for potential recursive divergence.

Usage Example:
>>> loop_data = {"trace_id": "abc123", "depth": 3, "pattern": "A → B → C → A"}
>>> detector = AnomalyLoopDetector()
>>> if detector.is_anomalous(loop_data):
...     print("Anomaly detected")
"""

from typing import Any, Dict


class AnomalyLoopDetector:
    """
    Analyzes loop traces and flags those with signatures
    inconsistent with expected recursive patterns.
    """

    def __init__(self, baseline_patterns: list[str] | None = None):
        self.baseline_patterns = baseline_patterns or [
            "A → B → C → A",
            "X → Y → Z → X",
            "init → run → close → init"
        ]

    def is_anomalous(self, loop_data: Dict[str, Any]) -> bool:
        """
        Determines if a loop's pattern is anomalous compared to known baselines.
        """
        pattern = loop_data.get("pattern")
        if not pattern:
            return False  # No pattern means no comparison

        return pattern not in self.baseline_patterns
