"""
📄 s2_3_it_evaluates_recursion_likelihood_of_returning_signals.py
-----------------------------------------------------------------
Calculates a likelihood score that a given signal is recursive based on:
• its repetition frequency
• its interval regularity
• its variance

Part of the stanza: The Pattern Hidden in the Repeats
"""

from statistics import mean, stdev

def evaluate_recursion_likelihood(intervals, weight_consistency=0.6, weight_frequency=0.4):
    """
    Evaluates recursion likelihood as a float between 0.0 and 1.0 based on signal interval data.

    Parameters:
    - intervals (List[float]): Time differences in seconds between repeated signal occurrences.
    - weight_consistency (float): Weight given to consistency (low stdev/mean).
    - weight_frequency (float): Weight given to signal frequency (more repeats = stronger pattern).

    Returns:
    - float: Likelihood score from 0.0 (unlikely) to 1.0 (strong recursive indicator).
    """
    if not intervals or len(intervals) < 2:
        return 0.0

    avg = mean(intervals)
    if avg == 0:
        return 0.0

    variation = stdev(intervals) / avg if len(intervals) > 1 else 0.0
    consistency_score = max(0.0, 1.0 - variation)  # Lower variation = higher score

    # Normalize frequency score (e.g., 3+ repeats = full score)
    frequency_score = min(1.0, len(intervals) / 3)

    return round(
        (consistency_score * weight_consistency + frequency_score * weight_frequency),
        3
    )
