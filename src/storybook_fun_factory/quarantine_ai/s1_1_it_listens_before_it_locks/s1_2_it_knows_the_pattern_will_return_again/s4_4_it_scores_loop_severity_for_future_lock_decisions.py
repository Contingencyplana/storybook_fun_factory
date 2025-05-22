"""
Filename: s4_4_it_scores_loop_severity_for_future_lock_decisions.py

Purpose:
This module computes a severity score for loop-confirmed anomalies based on
frequency, similarity, and velocity of signal recurrence. The score helps
determine whether soft pre-locks should escalate into full canonical locks.

Philosophy:
Not all loops are equal. Some whisper. Others roar. Severity is the key.

Example Usage:
    scorer = LoopSeverityScorer()
    score = scorer.score_signal(frequency=5, similarity=0.9, velocity=3.0)
    assert score > 0
"""

class LoopSeverityScorer:
    def score_signal(self, frequency: int, similarity: float, velocity: float) -> float:
        """
        Scores a signal based on:
        - frequency: number of times the signal recurred (higher = more dangerous)
        - similarity: match percentage to past trace [0.0 to 1.0]
        - velocity: time-based speed of recurrence (lower = more rapid = more severe)
        """
        base_score = frequency * similarity
        if velocity > 0:
            severity = base_score / velocity
        else:
            severity = base_score * 10  # cap to emphasize extreme velocity
        return round(severity, 2)
