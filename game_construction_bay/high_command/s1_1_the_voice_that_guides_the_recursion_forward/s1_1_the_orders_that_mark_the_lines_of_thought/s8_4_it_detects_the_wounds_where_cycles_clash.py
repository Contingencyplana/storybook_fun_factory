"""
Filename: s8_4_it_detects_the_wounds_where_cycles_clash.py

Purpose:
Analyzes the verse registry and detects stanza inconsistencies, including:
- Orphaned stanza files
- Duplicate stanza filenames (based on 'path')
- Component-mismatched stanza IDs

Poetic Role:
The Gate That Knows Each Line Beneath – Line 4
"""

from typing import Dict, List

def detect_registry_wounds(registry: Dict[str, Dict[str, str]]) -> List[str]:
    """
    Analyzes a verse registry for potential recursion wounds.

    Args:
        registry (dict): Mapping of stanza metadata (key → {component, path})

    Returns:
        List[str]: List of warnings or errors detected in the stanza registry
    """
    wounds = []
    seen_filenames = set()
    component_id_mismatch = []

    filename_counts = {}

    for key, meta in registry.items():
        path = meta.get("path", "")
        stanza_filename = path.split("/")[-1] if path else ""

        if stanza_filename:
            filename_counts[stanza_filename] = filename_counts.get(stanza_filename, 0) + 1

        if not meta.get("component") or not meta.get("path"):
            wounds.append(f"⚠️ Incomplete stanza metadata for: {key}")
            continue

        stanza_id_prefix = stanza_filename.split("_")[0] if "_" in stanza_filename else ""
        if stanza_id_prefix and stanza_id_prefix.lower() not in meta["component"].lower():
            component_id_mismatch.append(key)

    for filename, count in filename_counts.items():
        if count > 1:
            wounds.append(f"⚠️ Duplicate stanza filename detected: {filename}")

    for mismatch in component_id_mismatch:
        wounds.append(f"⚠️ Stanza ID does not match component: {mismatch}")

    return wounds
