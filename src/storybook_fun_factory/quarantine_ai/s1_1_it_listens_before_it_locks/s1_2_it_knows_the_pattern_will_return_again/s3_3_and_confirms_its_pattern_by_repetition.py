"""
Filename: s3_3_and_confirms_its_pattern_by_repetition.py

Purpose:
This module confirms pattern validity based on repeated echo match count.
A pattern is only considered confirmed after matching the same anomaly multiple times.

Philosophy:
Not every recurrence is truth. But truth, when it echoes thrice, begins to define a pattern.

Example Usage:
    confirmer = PatternConfirmer(repetition_threshold=3)
    for _ in range(3):
        confirmer.record_match("loop_delta")
    assert confirmer.is_confirmed("loop_delta") is True
"""

from collections import defaultdict

class PatternConfirmer:
    def __init__(self, repetition_threshold: int = 3):
        self.repetition_threshold = repetition_threshold
        self.match_count = defaultdict(int)

    def record_match(self, signal_id: str):
        self.match_count[signal_id] += 1

    def is_confirmed(self, signal_id: str) -> bool:
        return self.match_count[signal_id] >= self.repetition_threshold
