"""
_2_3_four_lines_compose_the_form_in_flame.py

Ensures that all stanza lines follow consistent structural encoding,
reinforcing both assistant logic and recursive recognition.
"""

import re


def enforce_stanza_consistency(filenames: list[str]) -> list[str]:
    """
    Ensures all filenames in a stanza:
    - Are lowercase
    - Contain only slug-case alphanumeric characters and underscores
    - Use single underscores consistently
    - End in '.py'

    Parameters:
        filenames (list[str]): A list of poetic filenames.

    Returns:
        list[str]: A list of normalized and validated filenames.
    """
    normalized = []
    for name in filenames:
        if not name or not isinstance(name, str):
            continue

        # Lowercase
        name = name.lower().strip()

        # Remove illegal characters (keep a-z, 0-9, _ and .)
        name = re.sub(r"[^\w\.]", "", name)

        # Collapse multiple underscores
        name = re.sub(r"_+", "_", name)

        # Remove leading/trailing underscores
        name = name.strip("_")

        # Ensure .py ending
        if not name.endswith(".py"):
            name = name + ".py"

        normalized.append(name)

    return normalized
