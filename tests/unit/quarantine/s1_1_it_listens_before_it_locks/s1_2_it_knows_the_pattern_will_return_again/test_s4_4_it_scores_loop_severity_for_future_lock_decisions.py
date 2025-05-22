"""
Test File: test_s4_4_it_scores_loop_severity_for_future_lock_decisions.py

Tests the LoopSeverityScorer from s4_4_it_scores_loop_severity_for_future_lock_decisions.py
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

# Import target module
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_2_it_knows_the_pattern_will_return_again",
        "s4_4_it_scores_loop_severity_for_future_lock_decisions.py"
    )
)

def test_score_signal_produces_reasonable_scores():
    scorer = module.LoopSeverityScorer()
    assert scorer.score_signal(frequency=5, similarity=0.9, velocity=2.0) > 0
    assert scorer.score_signal(frequency=3, similarity=0.5, velocity=1.0) > 0
    assert scorer.score_signal(frequency=2, similarity=1.0, velocity=0.0) > 10
