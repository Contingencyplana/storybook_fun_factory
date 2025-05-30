"""
Test File: test_s3_4_not_when_first_seen_but_when_reseen.py

Tests the EchoBasedFilter from s3_4_not_when_first_seen_but_when_reseen.py
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
        "s3_4_not_when_first_seen_but_when_reseen.py"
    )
)

def test_echo_based_filter_behavior():
    filter = module.EchoBasedFilter()
    assert filter.should_act("signal_x") is False
    assert filter.should_act("signal_x") is True
    assert filter.should_act("signal_y") is False
    assert filter.should_act("signal_y") is True
