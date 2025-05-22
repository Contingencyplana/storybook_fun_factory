"""
📄 s2_2_it_differentiates_repetition_from_coincidence.py
---------------------------------------------------------
Determines whether observed repetitions in signal intervals exceed a statistical threshold for non-randomness.

Part of the stanza: The Pattern Hidden in the Repeats
"""

from statistics import mean, stdev

def is_probable_pattern(intervals, min_repeats=3, variation_threshold=0.25):
    """
    Evaluates whether a list of time intervals suggests a non-coincidental recurrence pattern.

    Parameters:
    - intervals (List[float]): List of seconds between signal repeats.
    - min_repeats (int): Minimum number of intervals required to assess a pattern.
    - variation_threshold (float): Max allowed relative variation (stdev/mean) for pattern confirmation.

    Returns:
    - bool: True if repetition is likely non-coincidental, False otherwise.
    """
    if len(intervals) < min_repeats:
        return False

    avg = mean(intervals)
    if avg == 0:
        return False

    variation = stdev(intervals) / avg if len(intervals) > 1 else 0
    return variation <= variation_threshold
