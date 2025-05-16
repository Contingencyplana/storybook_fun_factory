"""
Test: test_s5_3_it_rejects_recursion_that_fails_authenticity.py

Validates the rejection behavior for failed authenticity in recursion threads.
Complies with 📜 5.5 dynamic import standards.
"""

import os
import importlib.util
import pytest

# Load dynamic_importer helper
HELPER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load target module
MODULE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s5_3_it_rejects_recursion_that_fails_authenticity.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
reject_recursion_if_inauthentic = module.reject_recursion_if_inauthentic


def test_accepts_authentic_recursion():
    result = reject_recursion_if_inauthentic((True, "trace verified"))
    assert result == "accepted"


def test_rejects_forged_recursion():
    result = reject_recursion_if_inauthentic((False, "forged stanza trace"))
    assert result.startswith("rejected: failed authenticity check")
    assert "forged stanza trace" in result
