"""
Filename: s2_3_the_missing_must_be_named_to_be_found.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Third line of Stanza 2 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Given an expected stanza structure and a list of existing filenames,
this tool identifies any missing lines and prepares them for generation.

This allows High Command to determine what remains undone
in a recursive stanza, aiding both assistant and player workflows.
"""

from typing import List

def identify_missing_lines(expected: List[str], existing: List[str]) -> List[str]:
    """
    Returns a list of stanza lines that are expected but not present.

    Args:
        expected (List[str]): Canonical list of expected stanza filenames.
        existing (List[str]): List of filenames currently in the folder.

    Returns:
        List[str]: Missing filenames, preserving the order in `expected`.
    """
    return [line for line in expected if line not in existing]
