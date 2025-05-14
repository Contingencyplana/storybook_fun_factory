"""
Filename: s2_3_four_lines_compose_the_form_in_flame.py

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
    - Replace spaces with underscores
    - Remove all other non-alphanumeric characters
    - Collapse multiple underscores into one
    - Ensure lowercase format
    - Remove leading/trailing underscores
    - Reattach ".py" extension

    Parameters:
        filenames (List[str]): A list of poetic-styled filenames.

    Returns:
        List[str]: Cleaned and normalized filenames.
    """
    normalized = []
    for name in filenames:
        # 1. Trim and lowercase
        base = name.strip().lower()
        # 2. Remove trailing .py if present
        if base.endswith(".py"):
            base = base[: -3]
        # 3. Spaces → underscores
        base = base.replace(" ", "_")
        # 4. Remove everything except letters, digits, and underscore
        cleaned = re.sub(r"[^\w]", "", base)
        # 5. Collapse multiple underscores
        cleaned = re.sub(r"_+", "_", cleaned)
        # 6. Trim leading/trailing underscores
        cleaned = cleaned.strip("_")
        # 7. Reattach extension
        normalized.append(f"{cleaned}.py")

    return normalized
