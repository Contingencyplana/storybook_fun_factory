"""
s1_1_a_verse_is_born_but_cannot_live.py

Begins the stanza by recognizing the poetic line as a latent construct—
existing in potential, but not executable without transformation.
"""

def poetic_line_status(poetic_line: str) -> str:
    if not poetic_line:
        return "latent"

    forbidden_chars = set('<>:"/\\|?*')
    poetic_invalid_tokens = ["'", ",", ".", "  "]  # Double spaces, quotes, commas

    if any(char in poetic_line for char in forbidden_chars):
        return "latent"
    if any(token in poetic_line for token in poetic_invalid_tokens):
        return "latent"
    if poetic_line != poetic_line.strip():
        return "latent"
    if poetic_line.lower() != poetic_line:
        return "latent"

    return "valid"
