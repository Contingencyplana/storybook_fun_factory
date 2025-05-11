"""
Test File: test_s1_4_it_confirms_the_new_phase_integrity.py

Tests the integrity verification logic after a recursive handoff.
Follows Dynamic Import Methodology as per 📜 5.5.
"""

import os
import importlib.util
import pytest

# ✅ Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically import the target module from game_construction_bay
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_2_the_transitions_that_shape_the_recursive_path",
    "s1_4_it_confirms_the_new_phase_integrity.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

def test_integrity_passes():
    context = {
        "post_log_verified": True,
        "memory_alignment_confirmed": True,
        "stanza_sync_complete": True
    }
    assert module.confirm_new_phase_integrity(context) is True

def test_missing_post_log():
    context = {
        "post_log_verified": False,
        "memory_alignment_confirmed": True,
        "stanza_sync_complete": True
    }
    assert module.confirm_new_phase_integrity(context) is False

def test_missing_memory_alignment():
    context = {
        "post_log_verified": True,
        "memory_alignment_confirmed": False,
        "stanza_sync_complete": True
    }
    assert module.confirm_new_phase_integrity(context) is False

def test_missing_stanza_sync():
    context = {
        "post_log_verified": True,
        "memory_alignment_confirmed": True,
        "stanza_sync_complete": False
    }
    assert module.confirm_new_phase_integrity(context) is False
