"""
s3_1_it_knows_what_has_been_canonized.py
(A Poetic-Memory Tracker for GDJ-to-Stanza Canon)

This High Command stanza line scans and maps canonical Game Development Journal (GDJ) entries 
to their corresponding stanza lines across Storybook FUN Factory. It ensures that each 
implemented file is recognized by the assistant as canonized, logged, and contextually 
anchored in memory.

Functional Roles:
- Index GDJ metadata (e.g., title, number, timestamp, stanza linkage).
- Validate that stanza files have been recorded in GDJs.
- Provide lookup methods for GDJ→Stanza and Stanza→GDJ.
- Prepare for future memory sync tools and dashboard surfacing.

This file complies with the Dynamic Import Test Methodology (📜 5.5).
"""

import os
import json
from typing import Optional, Dict, List, Tuple
from pathlib import Path


class CanonMemory:
    def __init__(self, gdj_index_path: Optional[Path] = None):
        self.gdj_index_path = gdj_index_path or Path.cwd() / "data" / "gdj_index.json"
        self._index = self._load_index()

    def _load_index(self) -> Dict:
        if not self.gdj_index_path.exists():
            return {}
        try:
            with self.gdj_index_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def is_canonized(self, stanza_path: str) -> bool:
        """Returns True if the stanza path is recorded in the GDJ index."""
        return any(entry.get("stanza_path") == stanza_path for entry in self._index.values())

    def get_gdj_by_stanza(self, stanza_path: str) -> Optional[Dict]:
        """Returns the GDJ metadata that matches a stanza path, if found."""
        for entry in self._index.values():
            if entry.get("stanza_path") == stanza_path:
                return entry
        return None

    def get_stanza_by_gdj(self, gdj_number: str) -> Optional[str]:
        """Returns the stanza path linked to a specific GDJ number, if found."""
        entry = self._index.get(gdj_number)
        return entry.get("stanza_path") if entry else None

    def list_all_canonized_pairs(self) -> List[Tuple[str, str]]:
        """Returns a list of (GDJ number, stanza path) pairs."""
        return [
            (gdj_num, entry["stanza_path"])
            for gdj_num, entry in self._index.items()
            if "stanza_path" in entry
        ]

    def list_unlinked_gdjs(self) -> List[str]:
        """Returns a list of GDJ numbers without stanza_path mappings."""
        return [
            gdj_num
            for gdj_num, entry in self._index.items()
            if "stanza_path" not in entry or not entry["stanza_path"]
        ]

    def reload(self):
        """Reload the index from disk, useful after file edits."""
        self._index = self._load_index()
