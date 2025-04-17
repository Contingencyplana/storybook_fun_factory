"""
_2_1_a_whisper_shaped_to_match_the_shell.py

Begins the second stanza by echoing the poetic line through syntactic rhythm—
formatting each name to retain its lyrical origin within structural bounds.
"""

import re


def format_poetic_slug(poetic_line: str) -> str:
    """
    Applies syntactic formatting to a poetic line to preserve its lyrical rhythm
    while preparing it for structured naming.

    Responsibilities:
    - Convert poetic lines into slug-style fragments while maintaining poetic pacing
    - Normalize spacing and underscores for recursive parsing
    - Preserve intentional underscore groupings (e.g., double underscores for pauses)

    Parameters:
        poetic_line (str): A cleaned, reshaped poetic line.

    Returns:
        str: A formatted, stylized poetic slug for filename usage.
    """
    if not poetic_line or not poetic_line.strip():
        return "unnamed_slug"

    # Collapse multiple spaces and replace them with underscores
    line = re.sub(r"\s{2,}", " ", poetic_line.strip())
    line = line.replace(" ", "_")

    # Preserve multiple underscores if explicitly present (poetic emphasis)
    line = re.sub(r"_+", lambda m: m.group(0), line)

    # Strip leading/trailing underscores
    return line.strip("_")
