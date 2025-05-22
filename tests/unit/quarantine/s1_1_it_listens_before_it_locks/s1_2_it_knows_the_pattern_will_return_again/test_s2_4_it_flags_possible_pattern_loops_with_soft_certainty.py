"""
🧪 test_s2_4_it_flags_possible_pattern_loops_with_soft_certainty.py
-------------------------------------------------------------------
Tests soft-flagging of suspected recursive loops using dynamic import (📜 5.5-compliant).
"""

import os
import importlib.util
import pytest

# 📦 Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# 📄 Load module under test
project_root = os.path.abspath(os.getcwd())
flag_module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s2_4_it_flags_possible_pattern_loops_with_soft_certainty.py"
)
flag_module = dynamic_importer.dynamic_import_module(flag_module_path)

# 📄 Load recursion likelihood module
likelihood_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s2_3_it_evaluates_recursion_likelihood_of_returning_signals.py"
)
likelihood_module = dynamic_importer.dynamic_import_module(likelihood_path)
likelihood_fn = likelihood_module.evaluate_recursion_likelihood

def test_flags_pattern_when_likelihood_is_high():
    intervals = [10.0, 10.1, 10.2, 9.9]
    flagged, score = flag_module.should_flag_pattern_loop(intervals, likelihood_fn)
    assert flagged is True
    assert score >= 0.75

def test_does_not_flag_low_confidence_pattern():
    intervals = [3.0, 33.0, 15.0]
    flagged, score = flag_module.should_flag_pattern_loop(intervals, likelihood_fn)
    assert flagged is False
    assert score < 0.75

def test_returns_exact_score_with_rounding():
    intervals = [12.0, 18.0, 15.0]
    flagged, score = flag_module.should_flag_pattern_loop(intervals, likelihood_fn)
    assert isinstance(score, float)
    assert round(score, 3) == score
