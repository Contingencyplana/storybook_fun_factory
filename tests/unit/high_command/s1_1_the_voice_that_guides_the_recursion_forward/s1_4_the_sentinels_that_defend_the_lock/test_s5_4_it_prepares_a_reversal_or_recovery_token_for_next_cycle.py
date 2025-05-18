"""
test_s5_4_it_prepares_a_reversal_or_recovery_token_for_next_cycle.py

Tests generation of structured recovery tokens.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s5_4_it_prepares_a_reversal_or_recovery_token_for_next_cycle as token_maker

def test_valid_token_structure():
    token = token_maker.prepare_recovery_token("anomX", "s5_3")
    assert isinstance(token["token_id"], str)
    assert token["anomaly_id"] == "anomX"
    assert token["stanza_id"] == "s5_3"
    assert token["strategy"] == "rollback"
    assert token["next_cycle"] == "lockdown_reversion_and_repair"
    assert "timestamp" in token

def test_custom_strategy_rebuild():
    token = token_maker.prepare_recovery_token("a2", "s5_2", strategy="rebuild")
    assert token["strategy"] == "rebuild"

def test_invalid_strategy_raises():
    with pytest.raises(ValueError):
        token_maker.prepare_recovery_token("z9", "s5_1", strategy="explode")
