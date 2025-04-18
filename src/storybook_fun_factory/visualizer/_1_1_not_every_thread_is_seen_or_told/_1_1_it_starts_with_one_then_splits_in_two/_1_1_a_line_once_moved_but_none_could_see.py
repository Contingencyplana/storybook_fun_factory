"""
_1_1_a_verse_is_born_but_cannot_live.py

Begins the stanza by recognizing the poetic line as a latent construct—
existing in potential, but not executable without transformation.
"""

from typing import Union


def is_poetic_line_valid(poetic_line: str) -> bool:
    """
    Checks if a poetic line contains only valid poetic characters
    and does not yet meet code-usable filename requirements.

    A poetic line is considered 'not alive' if:
    - It contains uppercase characters
    - It contains invalid characters (e.g., punctuation, symbols)
    - It contains leading/trailing whitespace
    - It uses poetic formatting (spaces, commas, apostrophes, etc.)

    Returns False if the line *could* be used as a filename already (i.e. is alive).
    """
    if not poetic_line:
        return False

    # Characters not allowed in filenames (esp. on Windows)
    forbidden_chars = set('<>:"/\\|?*')
    poetic_invalid_tokens = ["'", ",", ".", "  "]  # Double spaces, quotes, commas

    # Check structural formatting issues
    if any(char in poetic_line for char in forbidden_chars):
        return False
    if any(token in poetic_line for token in poetic_invalid_tokens):
        return False
    if poetic_line != poetic_line.strip():
        return False
    if poetic_line.lower() != poetic_line:
        return False  # still in poetic form (capitalized)

    # If all checks pass, it's already a usable name (and thus 'alive')
    return True  # the line has become structurally valid


def poetic_line_status(poetic_line: str) -> str:
    """
    Returns a human-readable status for a poetic line:
    - 'latent' if the line cannot live yet
    - 'valid' if the line can be used as-is
    """
    return "valid" if is_poetic_line_valid(poetic_line) else "latent"
