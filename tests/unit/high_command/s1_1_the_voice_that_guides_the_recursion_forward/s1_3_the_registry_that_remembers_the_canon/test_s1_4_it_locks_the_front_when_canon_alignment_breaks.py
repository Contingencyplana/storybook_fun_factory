"""
📄 test_s1_4_it_locks_the_front_when_canon_alignment_breaks.py

This test suite validates CanonLockout, confirming it enforces lockouts
on mismatch between registered and live stanza hashes.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_3_the_registry_that_remembers_the_canon.s1_4_it_locks_the_front_when_canon_alignment_breaks import CanonLockout

def test_canon_lockout_behavior():
    lockout = CanonLockout()

    canon_map = {
        "s1_1": "abc111",
        "s1_2": "def222",
        "s1_3": "ghi333",
        "s1_4": "jkl444"
    }

    # Register canonical hashes
    for stanza_id, canon_hash in canon_map.items():
        lockout.register_stanza(stanza_id, canon_hash)

    # Check matching hashes (should not lock)
    for stanza_id, canon_hash in canon_map.items():
        assert lockout.check_and_lock(stanza_id, canon_hash) is False

    # Check mismatched hashes (should lock)
    assert lockout.check_and_lock("s1_1", "zzz999")
    assert lockout.check_and_lock("s1_3", "")
    assert lockout.check_and_lock("s1_4", "jkl000")

    # Confirm lockable stanzas
    assert lockout.get_lockable_stanzas() == sorted(canon_map.keys())
