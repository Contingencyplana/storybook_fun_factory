"""
s2_2_it_identifies_unsanctioned_timestamp_or_commit.py

Flags files with unsanctioned edits based on either:
1. Modified timestamps newer than those recorded in a canonical timestamp registry.
2. Uncommitted changes in tracked Git files.

Expected timestamp registry format:
{
    "relative/path/to/file.py": "2024-05-17T12:34:56"
}

Example usage:
>>> from s2_2_it_identifies_unsanctioned_timestamp_or_commit import detect_timestamp_and_git_anomalies
>>> breaches = detect_timestamp_and_git_anomalies("path/to/timestamp_registry.json", "base/project/dir")
>>> print(breaches)
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List


def _load_timestamp_registry(path: Path) -> Dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _parse_iso_timestamp(ts: str) -> float:
    return datetime.fromisoformat(ts).timestamp()


def _get_git_modified_files(cwd: Path) -> List[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
        )
        modified = []
        for line in result.stdout.strip().split("\n"):
            if line and line[:2] in {" M", "MM", "A ", "AM", "??"}:
                modified.append(line[3:].strip())
        return modified
    except Exception:
        return []


def detect_timestamp_and_git_anomalies(
    registry_path: str, base_directory: str
) -> List[str]:
    registry = _load_timestamp_registry(Path(registry_path))
    root = Path(base_directory)
    flagged = []

    # Timestamp check
    for rel_path, recorded_time in registry.items():
        file_path = root / rel_path
        if not file_path.exists():
            flagged.append(rel_path)
            continue
        last_modified = file_path.stat().st_mtime
        canonical_time = _parse_iso_timestamp(recorded_time)
        if last_modified > canonical_time:
            flagged.append(rel_path)

    # Git uncommitted check
    git_flags = _get_git_modified_files(root)
    for rel_path in git_flags:
        if rel_path not in flagged and (root / rel_path).exists():
            flagged.append(rel_path)

    return sorted(set(flagged))
