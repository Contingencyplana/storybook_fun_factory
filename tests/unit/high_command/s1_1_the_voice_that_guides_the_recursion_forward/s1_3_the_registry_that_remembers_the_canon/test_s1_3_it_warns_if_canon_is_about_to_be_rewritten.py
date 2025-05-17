"""
📄 test_s1_3_it_warns_if_canon_is_about_to_be_rewritten.py

This test suite verifies CanonRewriteChecker logic, ensuring
that registered stanza hashes are protected against silent changes.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_3_the_registry_that_remembers_the_canon.s1_3_it_warns_if_canon_is_about_to_be_rewritten import CanonRewriteChecker

def test_register_and_warn_on_hash_changes():
    checker = CanonRewriteChecker()

    # Register stanzas and hashes
    canon_data = {
        "s1_1": "aaa111",
        "s1_2": "bbb222",
        "s1_3": "ccc333"
    }

    for stanza_id, hash_val in canon_data.items():
        checker.register_canon(stanza_id, hash_val)

    # Confirm no warnings on correct hashes
    for stanza_id, hash_val in canon_data.items():
        assert not checker.warn_if_changed(stanza_id, hash_val)

    # Confirm warnings on incorrect hashes
    assert checker.warn_if_changed("s1_1", "WRONG111")
    assert checker.warn_if_changed("s1_2", "WRONG222")
    assert checker.warn_if_changed("s1_3", "")

    # Confirm correct list of registered stanzas
    assert checker.get_registered_stanzas() == sorted(canon_data.keys())
