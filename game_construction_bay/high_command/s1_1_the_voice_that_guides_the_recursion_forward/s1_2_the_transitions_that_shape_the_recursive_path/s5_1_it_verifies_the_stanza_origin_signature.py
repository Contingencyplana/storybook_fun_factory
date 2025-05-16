"""
Filename: s5_1_it_verifies_the_stanza_origin_signature.py

Validates the origin signature of a stanza to ensure it matches a trusted source.
This file is the first line of defense in Stanza 1: The Chains That Must Not Break.

Fulfills Line 1 of Cycle 3 in s1_2_the_transitions_that_shape_the_recursive_path/.
"""

import json
from pathlib import Path
import hashlib

def calculate_file_signature(file_path: Path) -> str:
    """
    Calculates a SHA-256 hash of the file contents for signature comparison.

    Parameters:
    - file_path (Path): Path to the file to be hashed.

    Returns:
    - str: SHA-256 hash of the file contents.
    """
    with file_path.open("rb") as f:
        file_bytes = f.read()
        return hashlib.sha256(file_bytes).hexdigest()

def verify_stanza_origin_signature(file_path: Path, known_signature: str) -> bool:
    """
    Verifies that the origin signature of a stanza matches the expected value.

    Parameters:
    - file_path (Path): Path to the stanza file.
    - known_signature (str): The trusted SHA-256 hash to compare against.

    Returns:
    - bool: True if the signature matches, False otherwise.
    """
    actual_signature = calculate_file_signature(file_path)
    return actual_signature == known_signature
