"""
Test File: test_s4_1_it_deploys_a_shadow_trace_warning_if_loop_confirmed.py

Tests the ShadowTraceWarningSystem from s4_1_it_deploys_a_shadow_trace_warning_if_loop_confirmed.py
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

# Dynamic import of the target module
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_2_it_knows_the_pattern_will_return_again",
        "s4_1_it_deploys_a_shadow_trace_warning_if_loop_confirmed.py"
    )
)

def test_shadow_trace_warning():
    tracer = module.ShadowTraceWarningSystem()
    assert tracer.was_warned("loop_alpha") is False
    tracer.warn_if_loop_confirmed("loop_alpha", confirmed=True)
    assert tracer.was_warned("loop_alpha") is True
    tracer.warn_if_loop_confirmed("loop_beta", confirmed=False)
    assert tracer.was_warned("loop_beta") is False
