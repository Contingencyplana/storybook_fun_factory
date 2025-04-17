"""
_2_3_four_lines_compose_the_form_in_flame.py

Ensures that all stanza lines follow consistent structural encoding,
reinforcing both assistant logic and recursive recognition.
"""

import re
from typing import List


def enforce_stanza_consistency(filenames: List[str]) -> List[str]:
    """
    Cleans and normalizes poetic filenames to ensure stanza consistency.
    Applies strict formatting rules to ensure assistant logic can reliably parse
    and group related filenames.

    Rules:
    - Strip leading/trailing spaces and file extension
    - Remove all non-alphanumeric characters except underscores
    - Collapse multiple underscores
    - Strip leading/trailing underscores
    - Ensure lowercase format
    - Reattach ".py" extension

    Parameters:
        filenames (List[str]): A list of poetic-styled filenames.

    Returns:
        List[str]: Cleaned and normalized filenames.
    """
    normalized = []
    for name in filenames:
        base = name.strip().lower().replace(".py", "")

        # Remove all non-alphanumeric characters except underscore
        cleaned = re.sub(r"[^\w]", "_", base)

        # Collapse multiple underscores
        cleaned = re.sub(r"_+", "_", cleaned)

        # Strip leading/trailing underscores
        cleaned = cleaned.strip("_")

        normalized.append(f"{cleaned}.py")

    return normalized
