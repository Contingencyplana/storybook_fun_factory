"""
Test File: test_s4_3_it_enables_a_reversible_pre_lock_on_suspect_patterns.py

Tests the ReversiblePreLock from s4_3_it_enables_a_reversible_pre_lock_on_suspect_patterns.py
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
        "s4_3_it_enables_a_reversible_pre_lock_on_suspect_patterns.py"
    )
)

def test_reversible_pre_lock_behavior():
    lock = module.ReversiblePreLock()
    assert lock.is_locked("alpha") is False
    lock.pre_lock("alpha")
    assert lock.is_locked("alpha") is True
    lock.revoke("alpha")
    assert lock.is_locked("alpha") is False
