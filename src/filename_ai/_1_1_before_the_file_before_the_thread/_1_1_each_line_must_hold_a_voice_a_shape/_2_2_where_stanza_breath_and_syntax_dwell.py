"""
_2_2_where_stanza_breath_and_syntax_dwell.py

Introduces syntactic styling—balancing underscore rhythm, line pacing,
and filename readability to support recursive parsing.
"""

import re


def style_poetic_filename(poetic_filename: str) -> str:
    """
    Applies syntactic styling to a poetic filename to enhance rhythm and parsing clarity.

    Responsibilities:
    - Collapses triple or double underscores into single
    - Ensures no leading or trailing underscores
    - Preserves all lowercase slug formatting
    - Adds extra underscore between logical breaks (e.g., after every 4th word) if needed

    Parameters:
        poetic_filename (str): The unstyled poetic filename, assumed to be lowercase and underscore-based

    Returns:
        str: A syntactically styled filename string
    """
    if not poetic_filename or not poetic_filename.strip():
        return "unnamed_file"

    # Remove extension for internal styling
    name_core = poetic_filename.replace(".py", "")

    # Collapse multiple underscores
    name_core = re.sub(r"_+", "_", name_core)

    # Remove leading/trailing underscores
    name_core = name_core.strip("_")

    # Optionally: Break every 4 words with double underscore (stylistic spacing)
    words = name_core.split("_")
    styled = []
    for i, word in enumerate(words):
        styled.append(word)
        if (i + 1) % 4 == 0 and (i + 1) != len(words):
            styled.append("")  # Acts as double underscore when joined

    return "_".join(styled) + ".py"
