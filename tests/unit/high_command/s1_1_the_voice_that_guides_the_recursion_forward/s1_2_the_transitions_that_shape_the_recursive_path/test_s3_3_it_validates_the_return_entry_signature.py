"""
Test for s3_3_it_validates_the_return_entry_signature.py
Uses 📜 5.5-compliant dynamic import methodology.
"""

import os
import json
import importlib.util
from pathlib import Path
import pytest


def dynamic_import_module(module_path: str, module_name: str = "dynamic_module"):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def signature_file(tmp_path):
    def _write_signature(origin, layer):
        sig_path = tmp_path / "return_signature.json"
        content = {"origin": origin, "layer": layer, "signature_hash": "ABC123"}
        sig_path.write_text(json.dumps(content), encoding="utf-8")
        return sig_path
    return _write_signature


def test_signature_validation_logic(signature_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s3_3_it_validates_the_return_entry_signature.py"
        )
    )
    module = dynamic_import_module(module_path)

    # Valid case
    valid_sig = signature_file("dream_journal", "layer_2")
    assert module.validate_return_signature(valid_sig, "dream_journal", "layer_2") is True

    # Invalid origin
    bad_origin = signature_file("memory_ai", "layer_2")
    assert module.validate_return_signature(bad_origin, "dream_journal", "layer_2") is False

    # Invalid layer
    bad_layer = signature_file("dream_journal", "layer_1")
    assert module.validate_return_signature(bad_layer, "dream_journal", "layer_2") is False
