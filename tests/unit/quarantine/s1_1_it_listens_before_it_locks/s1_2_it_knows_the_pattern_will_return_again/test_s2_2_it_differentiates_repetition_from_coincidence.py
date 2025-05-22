"""
🧪 test_s2_2_it_differentiates_repetition_from_coincidence.py
--------------------------------------------------------------
Tests coincidence discrimination logic based on interval variation (📜 5.5-compliant).
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
    "s2_2_it_differentiates_repetition_from_coincidence.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_detects_pattern_with_low_variation():
    intervals = [10.0, 10.2, 9.8, 10.1]
    assert module.is_probable_pattern(intervals) is True

def test_detects_coincidence_with_high_variation():
    intervals = [2.0, 15.0, 7.5, 30.0]
    assert module.is_probable_pattern(intervals) is False

def test_requires_minimum_intervals():
    intervals = [12.0]
    assert module.is_probable_pattern(intervals) is False

def test_handles_zero_average():
    intervals = [0.0, 0.0, 0.0]
    assert module.is_probable_pattern(intervals) is False
