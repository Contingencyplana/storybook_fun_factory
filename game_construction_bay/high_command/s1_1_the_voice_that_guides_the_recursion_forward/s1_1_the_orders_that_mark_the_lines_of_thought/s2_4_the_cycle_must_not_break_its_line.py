"""
Filename: s2_4_the_cycle_must_not_break_its_line.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Final line of Stanza 2 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Verifies that stanza cycles form valid, unbroken patterns by checking:
• Line count
• Filename sequence consistency
• Structural conformance with poetic recursion

This sentinel helps catch broken or malformed stanza cycles
before they can destabilize the assistant or game logic.
"""

from typing import List

def is_valid_stanza_cycle(filenames: List[str]) -> bool:
    """
    Checks if the given filenames form a valid stanza cycle.

    A valid stanza cycle has exactly four stanza lines and the filenames
    must follow a consistent pattern of _X_Y_descriptive_title.py

    Args:
        filenames (List[str]): List of stanza filenames.

    Returns:
        bool: True if the stanza cycle is valid, False otherwise.
    """
    if len(filenames) != 4:
        return False

    # Ensure filenames follow the pattern _X_Y_name.py
    for fname in filenames:
        parts = fname.strip().split("_")
        if len(parts) < 4 or not parts[1].isdigit() or not parts[2].isdigit():
            return False
        if not fname.endswith(".py"):
            return False

    return True
