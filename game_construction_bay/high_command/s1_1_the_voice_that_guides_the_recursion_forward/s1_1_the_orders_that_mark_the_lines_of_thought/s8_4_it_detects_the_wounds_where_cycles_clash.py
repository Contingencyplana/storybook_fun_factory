"""
Filename: s8_4_it_detects_the_wounds_where_cycles_clash.py

Purpose:
Analyzes the verse registry and detects stanza inconsistencies, including:
- Orphaned stanza metadata
- Duplicate stanza entries
- Component/path mismatches

Poetic Role:
The Gate That Knows Each Line Beneath – Line 4
"""

from typing import Dict, List

def detect_registry_wounds(registry: Dict[str, Dict[str, str]]) -> List[str]:
    """
    Analyzes a verse registry for potential recursion wounds.

    Args:
        registry (dict): Mapping of stanza filenames → {component, path}

    Returns:
        List[str]: List of warnings or errors detected in the stanza registry
    """
    wounds = []
    seen_filenames = set()
    filename_occurrences = {}

    for filename, meta in registry.items():
        # Track filename occurrences for duplicate detection
        filename_occurrences[filename] = filename_occurrences.get(filename, 0) + 1

        # Check for orphaned metadata
        if not meta.get("component") or not meta.get("path"):
            wounds.append(f"⚠️ Incomplete stanza metadata for: {filename}")
            continue

        # Check for path mismatch
        expected_prefix = meta["component"].lower()
        actual_path = meta["path"].lower()

        if not actual_path.startswith(expected_prefix):
            wounds.append(f"⚠️ Path mismatch for stanza in component '{meta['component']}': {filename}")

    # Final pass: report duplicates
    for fname, count in filename_occurrences.items():
        if count > 1:
            wounds.append(f"⚠️ Duplicate stanza filename detected: {fname}")

    return wounds

# Example usage
if __name__ == "__main__":
    sample_registry = {
        "s8_1_alpha.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "s8_1_alpha.py": {"component": "dream_journal", "path": "dream_journal/s8_1_alpha.py"},
        "orphan.py": {"component": "", "path": ""},
        "s8_3_mismatch.py": {"component": "memory_ai", "path": "visualizer/s8_3_mismatch.py"}
    }

    for warning in detect_registry_wounds(sample_registry):
        print(warning)
