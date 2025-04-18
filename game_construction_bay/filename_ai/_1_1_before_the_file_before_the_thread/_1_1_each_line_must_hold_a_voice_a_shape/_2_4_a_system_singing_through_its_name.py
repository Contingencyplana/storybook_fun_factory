"""
_2_4_a_system_singing_through_its_name.py

Finalizes filename signature logic, embedding recursive awareness into each name
so the system can trace, parse, and narrate its own files.
"""

import re


def annotate_filename_with_signature(poetic_filename: str) -> str:
    """
    Appends a structured, recursive signature to a poetic filename.
    This enables both assistant traceability and narrative cohesion.

    Rules:
    - Normalize the filename (lowercase, strip, remove leading/trailing underscores)
    - Convert poetic spacing/punctuation to underscores
    - Remove extra underscores
    - Append a suffix "_sig" if no such suffix exists
    - Ensure the result ends with ".py"

    Parameters:
        poetic_filename (str): A poetic-style filename (may or may not be normalized).

    Returns:
        str: A syntactically aligned filename with embedded recursive signature.
    """
    # Strip leading/trailing spaces and remove .py if present
    name = poetic_filename.strip().lower()
    if name.endswith(".py"):
        name = name[:-3]

    # Normalize to underscores
    name = re.sub(r"[^\w]+", "_", name)  # Replace non-word chars with underscore
    name = re.sub(r"_+", "_", name)      # Collapse multiple underscores
    name = name.strip("_")               # Remove leading/trailing underscores

    # Add _sig if not present
    if not name.endswith("_sig"):
        name = f"{name}_sig"

    return f"{name}.py"
