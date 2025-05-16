"""
📄 test_s1_2_it_traces_the_stanza_to_its_origin.py

This test suite verifies the integrity of StanzaTraceRegistry,
ensuring all registered stanza metadata is accurately recorded,
validated, and retrievable.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_3_the_registry_that_remembers_the_canon.s1_2_it_traces_the_stanza_to_its_origin import StanzaTraceRegistry

def test_register_and_validate_traces():
    registry = StanzaTraceRegistry()

    # Dynamically register stanza entries
    stanzas = [
        ("s1_1", "📜 5.54", "abc123"),
        ("s1_2", "📜 5.55", "def456"),
        ("s1_3", "📜 5.56", "ghi789")
    ]

    for stanza_id, gdj, hash_val in stanzas:
        registry.register_stanza(stanza_id, gdj, hash_val)

    # Verify origins
    for stanza_id, gdj, _ in stanzas:
        assert registry.get_origin(stanza_id) == gdj

    # Confirm correct hash validation
    for stanza_id, _, hash_val in stanzas:
        assert registry.validate_hash(stanza_id, hash_val)

    # Confirm incorrect hashes are rejected
    assert not registry.validate_hash("s1_1", "wrong_hash")
    assert not registry.validate_hash("s1_2", "000000")

    # Confirm list_all_traced_stanzas returns expected values
    tracked_ids = registry.list_all_traced_stanzas()
    expected_ids = sorted([s[0] for s in stanzas])
    assert tracked_ids == expected_ids
