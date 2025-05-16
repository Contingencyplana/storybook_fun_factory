"""
Test: test_s5_1_it_verifies_the_stanza_origin_signature.py

Validates that the origin signature verification correctly matches or flags mismatch.
Uses 📜 5.5 dynamic import methodology.
"""

import os
import importlib.util
import hashlib
from pathlib import Path

import pytest

# Load dynamic_importer helper
HELPER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the module under test
MODULE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s5_1_it_verifies_the_stanza_origin_signature.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
verify_stanza_origin_signature = module.verify_stanza_origin_signature
calculate_file_signature = module.calculate_file_signature

def test_signature_matches(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_stanza.txt"
    test_file.write_text("trusted content")

    # Manually calculate signature
    known_signature = hashlib.sha256("trusted content".encode()).hexdigest()

    # Verify it matches
    assert verify_stanza_origin_signature(test_file, known_signature) is True

def test_signature_mismatch(tmp_path):
    # Create a test file with unexpected content
    test_file = tmp_path / "test_stanza.txt"
    test_file.write_text("malicious tampering")

    # Signature of trusted content (which this is not)
    wrong_signature = hashlib.sha256("trusted content".encode()).hexdigest()

    # Should not match
    assert verify_stanza_origin_signature(test_file, wrong_signature) is False
