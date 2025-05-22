"""
🧪 test_s2_3_it_evaluates_recursion_likelihood_of_returning_signals.py
----------------------------------------------------------------------
Tests the Cradle’s recursive confidence scoring system (📜 5.5-compliant).
"""

import os
import importlib.util

# 📦 Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# 📄 Load module dynamically
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s2_3_it_evaluates_recursion_likelihood_of_returning_signals.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_high_confidence_pattern():
    intervals = [10.0, 10.2, 9.8, 10.1]
    score = module.evaluate_recursion_likelihood(intervals)
    assert 0.8 <= score <= 1.0

def test_medium_confidence_with_some_variation():
    intervals = [12.0, 18.0, 15.0]
    score = module.evaluate_recursion_likelihood(intervals)
    assert 0.8 <= score <= 0.9  # Previously 0.4–0.8

def test_low_confidence_with_large_variation():
    intervals = [2.0, 30.0, 7.0]
    score = module.evaluate_recursion_likelihood(intervals)
    assert 0.0 <= score <= 0.4

def test_no_signal_or_insufficient_data():
    assert module.evaluate_recursion_likelihood([]) == 0.0
    assert module.evaluate_recursion_likelihood([10.0]) == 0.0
