"""
📄 s1_3_it_warns_if_canon_is_about_to_be_rewritten.py

This module detects when a file or stanza marked as canonical is at risk of being overwritten.
It issues preemptive warnings if a hash mismatch is found between a file's current state and its registered canonical state.

Functional Roles:
- Compares current file hash against known canon.
- Emits warnings when overwrite attempts are detected.
- Can be embedded into build pipelines or run as a standalone preflight check.

Example Usage:
>>> from s1_3_it_warns_if_canon_is_about_to_be_rewritten import CanonRewriteChecker
>>> checker = CanonRewriteChecker()
>>> checker.register_canon("s1_2", "abc123")
>>> checker.warn_if_changed("s1_2", "abc123")
False
>>> checker.warn_if_changed("s1_2", "zzz999")
True
"""

class CanonRewriteChecker:
    def __init__(self):
        self._canon_hashes = {}

    def register_canon(self, stanza_id: str, canon_hash: str) -> None:
        """Register the canonical hash of a stanza."""
        self._canon_hashes[stanza_id] = canon_hash

    def warn_if_changed(self, stanza_id: str, new_hash: str) -> bool:
        """Return True if the new hash differs from the canonical hash."""
        return self._canon_hashes.get(stanza_id) != new_hash

    def get_registered_stanzas(self) -> list[str]:
        """Return a list of all stanza IDs being monitored."""
        return sorted(self._canon_hashes.keys())
