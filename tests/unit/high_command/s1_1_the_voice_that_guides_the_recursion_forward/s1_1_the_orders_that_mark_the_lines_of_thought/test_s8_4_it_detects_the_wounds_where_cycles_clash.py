"""
Test File: test_s8_4_it_detects_the_wounds_where_cycles_clash.py

Tests the stanza wound detector from High Command Cycle 4, Stanza 1, Line 4.
Checks for orphaned stanza metadata, ID mismatches, and duplicate filenames.

Follows 📜 5.5 Dynamic Import methodology.
"""

import os
import sys
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

def test_detect_registry_wounds_with_issues():
    registry_with_issues = {
        "dream_s8_1_trace.py": {"component": "dream_journal", "path": "dream_journal/s8_1_trace.py"},
        "memory_s8_1_trace.py": {"component": "memory_ai", "path": "memory_ai/s8_1_trace.py"},
        "badmatch_s9_4_cross.py": {"component": "filename_ai", "path": "filename_ai/s9_4_cross.py"},
        "orphan.py": {"component": "", "path": ""}
    }

    result = detect_registry_wounds(registry_with_issues)

    assert any("Duplicate stanza filename" in r for r in result)
    assert any("Stanza ID does not match component" in r for r in result)
    assert any("Incomplete stanza metadata" in r for r in result)

def test_detect_registry_wounds_clean_registry():
    clean_registry = {
        "filename_ai_s8_1.py": {"component": "filename_ai", "path": "filename_ai/s8_1.py"},
        "memory_ai_s8_2.py": {"component": "memory_ai", "path": "memory_ai/s8_2.py"},
        "visualizer_s8_3.py": {"component": "visualizer", "path": "visualizer/s8_3.py"}
    }

    result = detect_registry_wounds(clean_registry)

    assert result == []
