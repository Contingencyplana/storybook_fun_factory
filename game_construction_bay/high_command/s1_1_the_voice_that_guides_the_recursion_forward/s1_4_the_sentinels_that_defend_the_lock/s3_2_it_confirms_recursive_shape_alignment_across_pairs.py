"""
s3_2_it_confirms_recursive_shape_alignment_across_pairs.py

Compares .meta.json files of mirrored stanza file pairs to ensure their recursive
trace_lineage (cycle, stanza, line) metadata is structurally aligned.

Expected mirror registry format:
[
    {
        "left_stanza_path": "path/to/stanzaA/",
        "right_stanza_path": "path/to/stanzaB/"
    },
    ...
]

Each file in stanzaA must have a matching file in stanzaB with the same name and:
- Matching `trace_lineage` metadata

Example usage:
>>> from s3_2_it_confirms_recursive_shape_alignment_across_pairs import check_shape_alignment
>>> mismatches = check_shape_alignment("mirror_pairs.json", base_directory=".")
>>> print(mismatches)
"""

import json
from pathlib import Path
from typing import List, Dict


def _load_registry(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_trace(file_path: Path) -> Dict:
    meta_path = file_path.with_suffix(".meta.json")
    if not meta_path.exists():
        return {}
    try:
        with meta_path.open("r", encoding="utf-8") as f:
            return json.load(f).get("trace_lineage", {})
    except Exception:
        return {}


def check_shape_alignment(
    mirror_registry_path: str, base_directory: str
) -> List[Dict[str, str]]:
    root = Path(base_directory)
    registry = _load_registry(Path(mirror_registry_path))
    issues = []

    for pair in registry:
        left = root / pair["left_stanza_path"]
        right = root / pair["right_stanza_path"]

        if not left.exists() or not right.exists():
            issues.append({"pair": pair, "reason": "Missing stanza folder(s)"})
            continue

        for left_file in sorted(left.glob("*.py")):
            right_file = right / left_file.name
            if not right_file.exists():
                issues.append({
                    "file": left_file.name,
                    "pair": pair,
                    "reason": "Missing mirrored file"
                })
                continue

            left_trace = _load_trace(left_file)
            right_trace = _load_trace(right_file)

            if left_trace != right_trace:
                issues.append({
                    "file": left_file.name,
                    "pair": pair,
                    "reason": "Trace lineage mismatch",
                    "left_trace": left_trace,
                    "right_trace": right_trace
                })

    return issues
