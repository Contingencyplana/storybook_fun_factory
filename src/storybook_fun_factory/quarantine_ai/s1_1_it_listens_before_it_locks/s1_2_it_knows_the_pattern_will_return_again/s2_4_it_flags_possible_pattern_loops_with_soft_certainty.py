"""
📄 s2_4_it_flags_possible_pattern_loops_with_soft_certainty.py
---------------------------------------------------------------
Combines interval analysis and recursion likelihood to raise soft warnings
for suspected recursive pattern loops.

Part of the stanza: The Pattern Hidden in the Repeats
"""

def should_flag_pattern_loop(intervals, likelihood_fn, threshold=0.75):
    """
    Uses a provided likelihood function to determine if the given intervals
    suggest a probable recursive loop worthy of soft flagging.

    Parameters:
    - intervals (List[float]): Time intervals between signal echoes.
    - likelihood_fn (Callable): Function to compute likelihood from intervals.
    - threshold (float): Minimum score to flag a loop (soft flag).

    Returns:
    - bool: True if loop pattern should be flagged, False otherwise.
    - float: The computed likelihood score.
    """
    score = likelihood_fn(intervals)
    return score >= threshold, round(score, 3)
