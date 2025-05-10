"""
Test File: test_s8_4_it_detects_the_wounds_where_cycles_clash.py

Tests the stanza wound detector from High Command Cycle 4, Stanza 1, Line 4.
Validates:
- Orphaned stanza metadata
- Duplicate stanza entries
- Component/path mismatches

Follows 📜 5.5 Dynamic Import Methodology.
"""

import os
import importlib.util
from pathlib import Path

# Load dynamic_importer
HELPER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py"))
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load target module dynamically
MODULE_PATH = os.path.abspath(
    os.path.join(
        Path.cwd(),
        "game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s8_4_it_detects_the_wounds_where_cycles_clash.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
detect_registry_wounds = module.detect_registry_wounds

def test_detect_registry_wounds_with_problems():
    registry_with_wounds = {
        "s8_1_alpha.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "s8_1_alpha.py": {"component": "memory_ai", "path": "memory_ai/s8_1_alpha.py"},  # Duplicate
        "s8_2_beta.py": {"component": "dream_journal", "path": "memory_ai/s8_2_beta.py"},  # Mismatch
        "s8_3_gamma.py": {"component": "", "path": ""}  # Orphan
    }

    results = detect_registry_wounds(registry_with_wounds)

    assert any("Duplicate stanza filename detected" in r for r in results)
    assert any("Path mismatch for stanza" in r for r in results)
    assert any("Incomplete stanza metadata" in r for r in results)

def test_detect_registry_wounds_clean_registry():
    clean_registry = {
        "s8_1_alpha.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "s8_2_beta.py": {"component": "memory_ai", "path": "memory_ai/s8_2_beta.py"},
        "s8_3_gamma.py": {"component": "visualizer", "path": "visualizer/s8_3_gamma.py"}
    }

    results = detect_registry_wounds(clean_registry)

    assert results == []
