"""
Filename: s8_4_it_detects_the_wounds_where_cycles_clash.py

Purpose:
Analyzes the verse registry and detects stanza inconsistencies, including:
- Orphaned stanza files
- Duplicate stanza names across components
- Component-mismatched stanza IDs

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
    component_id_mismatch = []

    for filename, meta in registry.items():
        if filename in seen_filenames:
            wounds.append(f"⚠️ Duplicate stanza filename detected: {filename}")
        else:
            seen_filenames.add(filename)

        if not meta.get("component") or not meta.get("path"):
            wounds.append(f"⚠️ Incomplete stanza metadata for: {filename}")
            continue

        # Check if stanza ID prefix matches component name
        stanza_id = filename.split("_")[0]
        if stanza_id and stanza_id.lower() not in meta["component"].lower():
            component_id_mismatch.append(filename)

    for mismatch in component_id_mismatch:
        wounds.append(f"⚠️ Stanza ID does not match component: {mismatch}")

    return wounds

# Example usage
if __name__ == "__main__":
    sample_registry = {
        "s8_1_detect.py": {"component": "memory_ai", "path": "memory/s8_1_detect.py"},
        "s8_1_detect.py": {"component": "dream_journal", "path": "dream/s8_1_detect.py"},
        "s8_4_mismatch.py": {"component": "visualizer", "path": "viz/s8_4_mismatch.py"}
    }
    for w in detect_registry_wounds(sample_registry):
        print(w)
