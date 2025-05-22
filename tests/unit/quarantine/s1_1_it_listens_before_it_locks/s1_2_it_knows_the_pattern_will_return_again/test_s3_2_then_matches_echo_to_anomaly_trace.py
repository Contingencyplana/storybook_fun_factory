"""
Test File: test_s3_2_then_matches_echo_to_anomaly_trace.py

Tests the EchoMatcher from s3_2_then_matches_echo_to_anomaly_trace.py
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
        "s3_2_then_matches_echo_to_anomaly_trace.py"
    )
)

def test_echo_matching_logic():
    matcher = module.EchoMatcher()
    matcher.remember_anomaly("signal_1", {"type": "glitch", "value": 42})
    assert matcher.match_echo("signal_1", {"type": "glitch", "value": 42}) is True
    assert matcher.match_echo("signal_1", {"type": "glitch", "value": 99}) is False
    assert matcher.match_echo("unknown", {"type": "glitch", "value": 42}) is False
