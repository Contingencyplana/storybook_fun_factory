"""
s4_1_it_detects_infinite_recursion_or_depth_overflow.py

Detects whether a recursive stanza execution has exceeded a safe depth threshold,
suggesting an infinite loop or runaway recursion.
"""

import sys
import logging

MAX_SAFE_RECURSION_DEPTH = 1000  # Configurable threshold
logger = logging.getLogger(__name__)

def detect_infinite_recursion(current_depth: int, max_depth: int = MAX_SAFE_RECURSION_DEPTH) -> bool:
    """
    Checks if the current recursion depth exceeds the safe limit.

    Args:
        current_depth (int): The current recursive call depth.
        max_depth (int): The threshold beyond which recursion is unsafe.

    Returns:
        bool: True if recursion depth exceeds max safe threshold, False otherwise.

    Example:
        >>> detect_infinite_recursion(1200)
        True
        >>> detect_infinite_recursion(800)
        False
    """
    if current_depth > max_depth:
        logger.warning(f"⚠️ Recursion depth {current_depth} exceeds safe threshold of {max_depth}.")
        return True
    return False
