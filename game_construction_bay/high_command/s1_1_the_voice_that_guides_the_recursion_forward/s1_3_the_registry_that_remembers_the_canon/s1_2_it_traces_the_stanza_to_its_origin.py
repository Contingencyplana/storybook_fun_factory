"""
📄 s1_2_it_traces_the_stanza_to_its_origin.py

This module establishes a system to trace each stanza back to its GDJ origin entry
and verify it against a persistent hash of its original logic. It ensures historical
integrity and protects against silent divergence.

Functional Roles:
- Link stanza files to their originating GDJ entries.
- Hash each stanza’s initial source code for validation.
- Provide lookup and comparison utilities.

Example Usage:
>>> from s1_2_it_traces_the_stanza_to_its_origin import StanzaTraceRegistry
>>> registry = StanzaTraceRegistry()
>>> registry.register_stanza("s1_1", "📜 5.54", "abc123hash")
>>> registry.get_origin("s1_1")
'📜 5.54'
>>> registry.validate_hash("s1_1", "abc123hash")
True
"""

class StanzaTraceRegistry:
    def __init__(self):
        self._registry = {}

    def register_stanza(self, stanza_id: str, gdj_ref: str, canonical_hash: str) -> None:
        """Register a stanza’s GDJ origin and its canonical hash."""
        self._registry[stanza_id] = {
            "gdj": gdj_ref,
            "hash": canonical_hash
        }

    def get_origin(self, stanza_id: str) -> str | None:
        """Retrieve the GDJ reference for a given stanza."""
        return self._registry.get(stanza_id, {}).get("gdj")

    def validate_hash(self, stanza_id: str, new_hash: str) -> bool:
        """Check if a new hash matches the registered canonical hash."""
        return self._registry.get(stanza_id, {}).get("hash") == new_hash

    def list_all_traced_stanzas(self) -> list[str]:
        """Return all stanza IDs currently tracked."""
        return sorted(self._registry.keys())
