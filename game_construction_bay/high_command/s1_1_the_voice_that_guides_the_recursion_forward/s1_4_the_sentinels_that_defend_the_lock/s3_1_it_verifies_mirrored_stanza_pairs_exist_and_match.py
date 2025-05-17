"""
s3_1_it_verifies_mirrored_stanza_pairs_exist_and_match.py

Verifies that each stanza listed in a canonical mirror-pair registry:
1. Exists at both mirrored locations
2. Contains the same number of stanza files
3. Has equivalent file names across each stanza (regardless of content)

Expected registry format:
[
    {
        "left_stanza_path": "path/to/stanzaA/",
        "right_stanza_path": "path/to/stanzaB/"
    },
    ...
]

Example usage:
>>> from s3_1_it_verifies_mirrored_stanza_pairs_exist_and_match import verify_mirrored_stanzas
>>> discrepancies = verify_mirrored_stanzas("mirror_pairs.json", base_directory=".")
>>> print(discrepancies)
"""

import json
from pathlib import Path
from typing import List, Dict


def _load_mirror_registry(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _list_filenames(directory: Path) -> List[str]:
    return sorted([f.name for f in directory.glob("*.py") if f.is_file()])


def verify_mirrored_stanzas(
    mirror_registry_path: str, base_directory: str
) -> List[Dict[str, str]]:
    root = Path(base_directory)
    registry = _load_mirror_registry(Path(mirror_registry_path))
    discrepancies = []

    for pair in registry:
        left_path = root / pair["left_stanza_path"]
        right_path = root / pair["right_stanza_path"]

        if not left_path.exists() or not right_path.exists():
            discrepancies.append({
                "pair": pair,
                "reason": "Missing one or both stanza folders"
            })
            continue

        left_files = _list_filenames(left_path)
        right_files = _list_filenames(right_path)

        if left_files != right_files:
            discrepancies.append({
                "pair": pair,
                "reason": "File mismatch",
                "left_files": left_files,
                "right_files": right_files
            })

    return discrepancies
