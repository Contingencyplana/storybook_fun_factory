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
    - Replace all non-alphanumeric characters (including dashes, dots, etc.) with underscores
    - Collapse multiple underscores
    - Remove leading/trailing underscores
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

        # Replace all non-alphanumerics with underscores
        cleaned = re.sub(r"[^\w]", "_", base)

        # Collapse multiple underscores
        cleaned = re.sub(r"_+", "_", cleaned)

        # Remove leading/trailing underscores
        cleaned = cleaned.strip("_")

        normalized.append(f"{cleaned}.py")

    return normalized
