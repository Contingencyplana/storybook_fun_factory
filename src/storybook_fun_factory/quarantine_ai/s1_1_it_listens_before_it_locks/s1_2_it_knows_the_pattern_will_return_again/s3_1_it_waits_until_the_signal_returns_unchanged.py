"""
Filename: s3_1_it_waits_until_the_signal_returns_unchanged.py

Purpose:
This module implements a soft-recursive signal deferral strategy.
It stores initial anomaly signals without acting, and only triggers evaluation
when the same signal returns unchanged after a defined delay period.

Philosophy:
Not all signals deserve immediate judgment. Some must be seen twice—
only upon return does their truth become clear.

Example Usage:
    evaluator = DeferredSignalEvaluator(delay_threshold=2)
    evaluator.record_signal("anomaly_xyz")
    assert evaluator.evaluate("anomaly_xyz") is False
    evaluator.record_signal("anomaly_xyz")
    assert evaluator.evaluate("anomaly_xyz") is True
"""

import time
from collections import defaultdict

class DeferredSignalEvaluator:
    def __init__(self, delay_threshold: int = 1):
        self.delay_threshold = delay_threshold
        self.signal_log = defaultdict(list)

    def record_signal(self, signal_id: str):
        self.signal_log[signal_id].append(time.time())

    def evaluate(self, signal_id: str) -> bool:
        timestamps = self.signal_log[signal_id]
        if len(timestamps) < 2:
            return False
        # Check if signal reappeared after delay_threshold seconds
        return (timestamps[-1] - timestamps[-2]) >= self.delay_threshold
