"""
s2_3_it_triggers_alerts_on_id_or_trace_discrepancy.py

This enforcement tool compares a current file ID and trace lineage against a canonical registry.
It raises an alert if:
1. The file ID (UUID or hash ID) does not match the registered version.
2. The trace lineage metadata (e.g., stanza_id or cycle_path) is tampered, missing, or mismatched.

Expected registry format:
{
    "relative/path/to/file.py": {
        "file_id": "uuid-or-hash",
        "trace_lineage": {
            "cycle": "recursion_enforcement_protocols",
            "stanza": "stanza_2",
            "line": "s2_3"
        }
    },
    ...
}

Example usage:
>>> from s2_3_it_triggers_alerts_on_id_or_trace_discrepancy import detect_id_and_trace_discrepancies
>>> issues = detect_id_and_trace_discrepancies("path/to/trace_registry.json", "base/project/dir")
>>> print(issues)
"""

import json
from pathlib import Path
from typing import Dict, List


def _load_trace_registry(path: Path) -> Dict[str, Dict]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_file_metadata(file_path: Path) -> Dict:
    metadata_path = file_path.with_suffix(".meta.json")
    if not metadata_path.exists():
        return {}
    with metadata_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def detect_id_and_trace_discrepancies(
    registry_path: str, base_directory: str
) -> List[str]:
    registry = _load_trace_registry(Path(registry_path))
    root = Path(base_directory)
    flagged = []

    for rel_path, expected in registry.items():
        file_path = root / rel_path
        metadata = _load_file_metadata(file_path)

        if not file_path.exists() or not metadata:
            flagged.append(rel_path)
            continue

        if metadata.get("file_id") != expected.get("file_id"):
            flagged.append(rel_path)
            continue

        expected_trace = expected.get("trace_lineage", {})
        actual_trace = metadata.get("trace_lineage", {})

        if expected_trace != actual_trace:
            flagged.append(rel_path)

    return sorted(set(flagged))
