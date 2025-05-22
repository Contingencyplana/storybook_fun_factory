"""
Test File: test_s3_1_it_waits_until_the_signal_returns_unchanged.py

Tests the DeferredSignalEvaluator from s3_1_it_waits_until_the_signal_returns_unchanged.py
using the dynamic import methodology (📜 5.5).
"""

import os
import time
import importlib.util
import pytest

# Load dynamic_importer.py helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
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
        "s1_2_it_knows_the_pattern_will_return_again",
        "deferred_signal_evaluation",
        "s1_1_it_waits_until_the_signal_returns_unchanged.py"
    )
)

def test_signal_deferral_logic():
    evaluator = module.DeferredSignalEvaluator(delay_threshold=1)
    evaluator.record_signal("loop_alpha")
    assert evaluator.evaluate("loop_alpha") is False
    time.sleep(1.1)
    evaluator.record_signal("loop_alpha")
    assert evaluator.evaluate("loop_alpha") is True
