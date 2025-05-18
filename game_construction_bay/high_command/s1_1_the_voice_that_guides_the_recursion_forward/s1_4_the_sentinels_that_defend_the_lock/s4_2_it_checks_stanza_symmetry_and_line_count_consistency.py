"""
s4_2_it_checks_stanza_symmetry_and_line_count_consistency.py

Checks whether a stanza (a group of four files) exhibits structural symmetry:
- It must contain exactly 4 lines
- Each line must follow canonical stanza filename conventions
"""

import re
from typing import List

EXPECTED_LINE_COUNT = 4
FILENAME_PATTERN = re.compile(r'^s\d_\d+_it_.*\.py$')

def check_stanza_symmetry(file_names: List[str]) -> bool:
    """
    Validates that a stanza is structurally sound.

    Args:
        file_names (List[str]): List of filenames within the stanza folder.

    Returns:
        bool: True if stanza has 4 validly-named lines, False otherwise.

    Example:
        >>> check_stanza_symmetry([
        ...     's4_1_it_detects_infinite_recursion_or_depth_overflow.py',
        ...     's4_2_it_checks_stanza_symmetry_and_line_count_consistency.py',
        ...     's4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py',
        ...     's4_4_it_logs_anomalies_without_halting_execution_yet.py'
        ... ])
        True
    """
    if len(file_names) != EXPECTED_LINE_COUNT:
        return False
    return all(FILENAME_PATTERN.match(f) for f in file_names)
