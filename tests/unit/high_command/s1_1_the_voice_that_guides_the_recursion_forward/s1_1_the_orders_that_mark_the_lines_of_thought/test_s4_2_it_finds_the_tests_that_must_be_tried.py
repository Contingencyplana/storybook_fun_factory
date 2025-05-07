"""
Filename: test_s4_2_it_finds_the_tests_that_must_be_tried.py

Tests the functionality of s4_2_it_finds_the_tests_that_must_be_tried.py using dynamic import,
as outlined in 📜 5.5. Ensures correct detection of in-progress test files from a status map.
"""

import os
import importlib.util
import pytest

# ✅ Load the dynamic importer helper module
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)

spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Construct absolute path to the target stanza file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
target_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s4_2_it_finds_the_tests_that_must_be_tried.py"
)

# ✅ Dynamically import the target module
module = dynamic_importer.dynamic_import_module(target_path)

# ✅ Access functions to test
find_pending_tests = module.find_pending_tests


def test_finds_only_tests_in_progress():
    mock_status = {
        "test_file_1.py": "[⏳ In progress]",
        "non_test_file.py": "[⏳ In progress]",
        "test_file_2.py": "[✅ Success!]",
        "test_file_3.py": "[⏳ In progress]",
    }

    result = find_pending_tests(mock_status)
    assert result == ["test_file_1.py", "test_file_3.py"]


def test_returns_empty_list_if_no_matches():
    mock_status = {
        "test_file_1.py": "[✅ Success!]",
        "test_file_2.py": "[✅ Success!]",
        "non_test_file.py": "[⏳ In progress]",
    }

    result = find_pending_tests(mock_status)
    assert result == []


def test_custom_marker_recognition():
    mock_status = {
        "test_alpha.py": "[WAITING]",
        "test_beta.py": "[WAITING]",
        "test_gamma.py": "[✅ Success!]",
    }

    result = find_pending_tests(mock_status, marker="[WAITING]")
    assert result == ["test_alpha.py", "test_beta.py"]
