"""
Filename: s1_3_the_line_must_twist_the_word_must_bend.py

Handles poetic reshaping—ensuring illegal or ambiguous verse fragments
are adapted into filename-safe and assistant-usable identifiers.
"""

import re


def reshape_poetic_line(poetic_line: str) -> str:
    """
    Reshapes a poetic line by pre-processing ambiguous or stylistically inconsistent
    fragments before they are converted into filenames.

    Responsibilities:
    - Normalize dash, em-dash, and hyphen variants to a single space
    - Replace stylized quotes or smart punctuation with safe equivalents
    - Remove dangling special characters from beginning or end (but preserve quotes and ellipses)
    - Replace multiple space clusters with a single space
    - Preserve case for downstream filename formatting

    Parameters:
        poetic_line (str): A potentially malformed or stylistically inconsistent poetic line.

    Returns:
        str: A normalized, reshaped poetic line ready for transformation.
    """
    if not poetic_line or not poetic_line.strip():
        return ""

    # Normalize dashes (— – −) and hyphens to space
    line = re.sub(r"[‐‑–—−]", " ", poetic_line)

    # Replace curly quotes and ellipses with plain equivalents
    replacements = {
        "“": "\"", "”": "\"",
        "‘": "'", "’": "'",
        "…": "...",
    }
    for bad, good in replacements.items():
        line = line.replace(bad, good)

    # Remove leading/trailing characters except letters, numbers, quotes, and periods
    line = re.sub(r"^[^A-Za-z0-9\"'\.]+|[^A-Za-z0-9\"'\.]+$", "", line)

    # Collapse multiple spaces
    line = re.sub(r"\s{2,}", " ", line)

    return line
