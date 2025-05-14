"""
Filename: s1_4_to_meet_the_code_yet_not_transcend.py

Completes the stanza by resolving syntax alignment, validating output,
and enforcing naming conventions that echo the line’s poetic source.
"""

import re


def validate_final_filename(poetic_filename: str) -> bool:
    """
    Validates that a poetic filename meets the structural and poetic standards
    for recursive use across Storybook FUN Factory systems.

    Rules enforced:
    - Must end in '.py'
    - Must be all lowercase
    - Must contain only valid slug characters: lowercase letters, digits, and underscores
    - Cannot start or end with an underscore
    - Cannot contain double underscores '__'
    - Must not exceed 100 characters
    - Must not be a reserved Python word (e.g., "def.py", "class.py")

    Parameters:
        poetic_filename (str): The filename to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not poetic_filename.endswith(".py"):
        return False

    name = poetic_filename[:-3]  # Strip .py

    if len(name) == 0 or len(name) > 100:
        return False

    if not name.islower():
        return False

    if re.search(r"[^a-z0-9_]", name):
        return False

    if name.startswith("_") or name.endswith("_"):
        return False

    if "__" in name:
        return False

    reserved = {"def", "class", "import", "return", "global", "lambda", "try", "except"}
    if name in reserved:
        return False

    return True
