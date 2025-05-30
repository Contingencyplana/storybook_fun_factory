"""
Test File: test_s4_2_it_defines_a_delay_zone_for_soft_containment.py

Tests the DelayZone from s4_2_it_defines_a_delay_zone_for_soft_containment.py
using the dynamic import methodology (📜 5.5).
"""

import os
import time
import importlib.util
import pytest

# Load dynamic_importer.py helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Import the target module
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "quarantine_ai",
        "s1_1_it_listens_before_it_locks",
        "s1_2_it_knows_the_pattern_will_return_again",
        "s4_2_it_defines_a_delay_zone_for_soft_containment.py"
    )
)

def test_delay_zone_behavior():
    delay_zone = module.DelayZone(delay_seconds=1)
    start = time.perf_counter()
    delay_zone.enter("loop_x")  # First entry — no delay
    delay_zone.enter("loop_x")  # Second entry — delay applied
    end = time.perf_counter()
    assert end - start >= 1
