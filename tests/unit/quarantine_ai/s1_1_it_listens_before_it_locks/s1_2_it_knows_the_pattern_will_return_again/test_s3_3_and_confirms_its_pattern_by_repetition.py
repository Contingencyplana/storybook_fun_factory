"""
Test File: test_s3_3_and_confirms_its_pattern_by_repetition.py

Tests the PatternConfirmer from s3_3_and_confirms_its_pattern_by_repetition.py
using the dynamic import methodology (📜 5.5).
"""

import os
import importlib.util
import pytest

# Load dynamic_importer.py helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Define project root and module path
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_2_it_knows_the_pattern_will_return_again",
        "s3_3_and_confirms_its_pattern_by_repetition.py"
    )
)

def test_pattern_confirmer_repetition():
    confirmer = module.PatternConfirmer(repetition_threshold=3)
    assert confirmer.is_confirmed("loop_beta") is False
    confirmer.record_match("loop_beta")
    assert confirmer.is_confirmed("loop_beta") is False
    confirmer.record_match("loop_beta")
    assert confirmer.is_confirmed("loop_beta") is False
    confirmer.record_match("loop_beta")
    assert confirmer.is_confirmed("loop_beta") is True
