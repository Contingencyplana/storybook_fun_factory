"""
_1_2_until_a_name_the_form_must_give.py

Implements the first transformation layer, assigning a structural name
to the poetic line while preserving rhythm and narrative cohesion.
"""

import re


def poetic_line_to_filename(poetic_line: str) -> str:
    """
    Transforms a poetic line into a valid, stylized Python filename.

    Rules:
    - Lowercase all characters
    - Replace spaces with underscores
    - Strip leading/trailing whitespace
    - Remove all non-alphanumeric characters except underscores
    - Collapse multiple underscores into one
    - Ensure the result ends in '.py'

    Parameters:
        poetic_line (str): The poetic input line.

    Returns:
        str: The transformed, code-valid filename.
    """
    if not poetic_line or not poetic_line.strip():
        return "unnamed_line.py"

    # Lowercase and strip
    name = poetic_line.lower().strip()

    # Replace all non-alphanumeric characters (except spaces) with nothing
    name = re.sub(r"[^\w\s]", "", name)

    # Replace all whitespace with underscores
    name = re.sub(r"\s+", "_", name)

    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)

    # Ensure it ends with .py
    return f"{name}.py"
