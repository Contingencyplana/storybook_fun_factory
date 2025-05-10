"""
Filename: s8_4_it_detects_the_wounds_where_cycles_clash.py

Purpose:
Analyzes the verse registry and detects stanza inconsistencies, including:
- Orphaned stanza records
- Repeated paths across entries (even with unique keys)
- Component mismatch between declared name and actual path

Poetic Role:
The Gate That Knows Each Line Beneath – Line 4
"""

from typing import Dict, List
from collections import Counter

def detect_registry_wounds(registry: Dict[str, Dict[str, str]]) -> List[str]:
    """
    Analyzes a verse registry for potential recursion wounds.

    Args:
        registry (dict): Mapping of stanza filenames → {component, path}

    Returns:
        List[str]: List of warnings or errors detected in the stanza registry
    """
    wounds = []
    path_counter = Counter()
    component_mismatches = []

    # Pass 1 – count paths, validate records
    for filename, meta in registry.items():
        component = meta.get("component", "").strip()
        path = meta.get("path", "").strip()

        # Orphan check
        if not component or not path:
            wounds.append(f"⚠️ Incomplete stanza metadata for: {filename}")
            continue

        path_counter[path] += 1

        # Check if component string appears in path
        if component not in path:
            component_mismatches.append(filename)

    # Pass 2 – evaluate path frequency
    for path, count in path_counter.items():
        if count > 1:
            wounds.append(f"⚠️ Duplicate stanza path detected: {path}")

    for mismatch in component_mismatches:
        wounds.append(f"⚠️ Stanza path does not match declared component: {mismatch}")

    return wounds

# Example usage
if __name__ == "__main__":
    registry = {
        "alpha_1.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "alpha_2.py": {"component": "memory_ai", "path": "filename_ai/s8_1_alpha.py"},  # duplicate path
        "beta.py": {"component": "dream_journal", "path": "memory_ai/s8_2_beta.py"},    # mismatch
        "orphan.py": {"component": "", "path": ""}                                      # orphan
    }

    for issue in detect_registry_wounds(registry):
        print(issue)
