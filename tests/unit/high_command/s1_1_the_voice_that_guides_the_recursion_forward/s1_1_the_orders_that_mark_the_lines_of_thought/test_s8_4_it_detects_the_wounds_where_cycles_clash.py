"""
Test File: test_s8_4_it_detects_the_wounds_where_cycles_clash.py

Tests the stanza wound detector from High Command Cycle 4, Stanza 1, Line 4.
Validates:
- Orphan stanza metadata
- Mismatched component/path stanza entries
- Duplicate stanza paths across registry
Follows 📜 5.5 Dynamic Import methodology.
"""

import os
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer
HELPER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py"))
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the target module dynamically
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
        "alpha_1.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "alpha_2.py": {"component": "memory_ai", "path": "filename_ai/s8_1_alpha.py"},  # Intentional duplicate path
        "beta.py": {"component": "dream_journal", "path": "memory_ai/s8_2_beta.py"},  # Mismatch
        "orphan.py": {"component": "", "path": ""}  # Orphan
    }

    results = detect_registry_wounds(registry_with_wounds)

    assert any("Duplicate stanza path detected" in r for r in results)
    assert any("Stanza path does not match declared component" in r for r in results)
    assert any("Incomplete stanza metadata" in r for r in results)

def test_detect_registry_wounds_clean_registry():
    clean_registry = {
        "alpha.py": {"component": "filename_ai", "path": "filename_ai/s8_1_alpha.py"},
        "beta.py": {"component": "memory_ai", "path": "memory_ai/s8_2_beta.py"},
        "gamma.py": {"component": "visualizer", "path": "visualizer/s8_3_gamma.py"}
    }

    results = detect_registry_wounds(clean_registry)

    assert results == []
