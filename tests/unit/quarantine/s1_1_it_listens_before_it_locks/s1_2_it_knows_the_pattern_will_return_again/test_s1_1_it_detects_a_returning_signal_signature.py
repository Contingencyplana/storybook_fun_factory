# test_s1_1_it_detects_a_returning_signal_signature.py

import pytest
from storybook_fun_factory.quarantine_ai.s1_1_it_listens_before_it_locks.s1_2_it_knows_the_pattern_will_return_again.s1_1_it_detects_a_returning_signal_signature import detect_returning_signals

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
