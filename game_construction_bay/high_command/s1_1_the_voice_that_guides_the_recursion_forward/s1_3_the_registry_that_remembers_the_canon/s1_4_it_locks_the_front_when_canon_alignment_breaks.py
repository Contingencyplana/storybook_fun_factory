"""
📄 s1_4_it_locks_the_front_when_canon_alignment_breaks.py

This module enforces a hard pause if a mismatch is detected between
current and canonical stanza structures. It represents the defensive
edge of the registry system — halting recursion or triggering alerts
when something fundamental is out of alignment.

Functional Roles:
- Compares expected vs. actual stanza hashes.
- Halts execution or returns critical status when misalignment is found.
- Supports audit logs for deferred analysis or automated lockout enforcement.

Example Usage:
>>> from s1_4_it_locks_the_front_when_canon_alignment_breaks import CanonLockout
>>> lockout = CanonLockout()
>>> lockout.register_stanza("s1_4", "zzz888")
>>> lockout.check_and_lock("s1_4", "zzz888")
False
>>> lockout.check_and_lock("s1_4", "wrong_hash")
True
"""

class CanonLockout:
    def __init__(self):
        self._canon_map = {}

    def register_stanza(self, stanza_id: str, canon_hash: str) -> None:
        """Register the canonical hash for a stanza."""
        self._canon_map[stanza_id] = canon_hash

    def check_and_lock(self, stanza_id: str, live_hash: str) -> bool:
        """
        Return True if lockout should occur (hash mismatch).
        Return False if canon and live match.
        """
        return self._canon_map.get(stanza_id) != live_hash

    def get_lockable_stanzas(self) -> list[str]:
        """Return all stanza IDs subject to lockout checks."""
        return sorted(self._canon_map.keys())
