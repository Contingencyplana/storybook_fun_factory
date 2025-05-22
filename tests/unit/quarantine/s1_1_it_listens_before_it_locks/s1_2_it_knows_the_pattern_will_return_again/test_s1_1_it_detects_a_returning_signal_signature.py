# test_s1_1_it_detects_a_returning_signal_signature.py

"""
Tests the detect_returning_signals function from s1_1_it_detects_a_returning_signal_signature.py.
Uses the Dynamic Import Test Methodology (📜 5.5) for compatibility with Poetry, recursion, and src layout.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer.py
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the target module
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s1_1_it_detects_a_returning_signal_signature.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

# ✅ Extract the function
detect_returning_signals = module.detect_returning_signals

# ✅ Tests
@pytest.mark.parametrize("signal_log,window,expected", [
    (["a", "b", "c", "a", "d", "b"], 100, {"a": 2, "b": 2}),
    (["x", "y", "z"], 100, {}),
    (["m", "n", "m", "m", "o", "n"], 100, {"m": 3, "n": 2}),
    (["r", "s", "t", "u", "r", "v", "r"], 5, {"r": 2}),
    ([], 100, {}),
])
def test_detect_returning_signals(signal_log, window, expected):
    result = detect_returning_signals(signal_log, memory_window=window)
    assert result == expected
