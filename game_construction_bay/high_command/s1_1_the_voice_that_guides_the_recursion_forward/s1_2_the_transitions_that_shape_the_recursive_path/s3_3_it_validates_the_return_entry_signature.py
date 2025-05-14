"""
Filename: s3_3_it_validates_the_return_entry_signature.py

Confirms whether a return trace from an async or layered recursion matches
a valid and expected reintegration signature.

Signatures represent canonical identity, expected recursion layer, and origin.
"""

import json
from pathlib import Path


def validate_return_signature(signature_path: Path, expected_origin: str, expected_layer: str) -> bool:
    """
    Validates a return signature to ensure correct reintegration into primary canon.

    Args:
        signature_path (Path): Path to the JSON file containing return signature metadata.
            Expected keys: 'origin', 'layer', 'signature_hash'
        expected_origin (str): The expected origin name or ID.
        expected_layer (str): The expected recursion layer.

    Returns:
        bool: True if signature is valid and matches expected values, False otherwise.

    Example:
        >>> validate_return_signature(Path("signature.json"), "dream_journal", "layer_2")
        True
    """
    if not signature_path.exists():
        raise FileNotFoundError(f"Signature file not found: {signature_path}")

    with open(signature_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    origin = data.get("origin")
    layer = data.get("layer")

    return origin == expected_origin and layer == expected_layer
