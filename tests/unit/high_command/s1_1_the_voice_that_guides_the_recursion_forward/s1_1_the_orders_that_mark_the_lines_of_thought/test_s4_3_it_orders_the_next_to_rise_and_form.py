"""
Filename: test_s4_3_it_orders_the_next_to_rise_and_form.py

Tests the functionality of s4_3_it_orders_the_next_to_rise_and_form.py using dynamic import,
following the canonical methodology defined in 📜 5.5.
"""

import os
import importlib.util

# ✅ Load the dynamic importer helper module
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically load the target stanza module
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
target_path = os.path.join(
    project_root,
    "game_construction_bay",
    "high_command",
    "s1_1_the_voice_that_guides_the_recursion_forward",
    "s1_1_the_orders_that_mark_the_lines_of_thought",
    "s4_3_it_orders_the_next_to_rise_and_form.py"
)
module = dynamic_importer.dynamic_import_module(target_path)

# ✅ Access functions from the module
find_next_creation_target = module.find_next_creation_target
issue_creation_instruction = module.issue_creation_instruction


def test_find_next_creation_target_returns_correct_file():
    mock_status = {
        "file_a.py": "[✅ Success!]",
        "file_b.py": "[🔜 Not started]",
        "file_c.py": "[⏳ In progress]",
    }
    assert find_next_creation_target(mock_status) == "file_b.py"


def test_find_next_creation_target_returns_none_if_all_started():
    mock_status = {
        "file_a.py": "[✅ Success!]",
        "file_b.py": "[⏳ In progress]",
        "file_c.py": "[✅ Success!]",
    }
    assert find_next_creation_target(mock_status) is None


def test_issue_creation_instruction_returns_expected_dispatch():
    instruction = issue_creation_instruction("file_b.py")
    assert "file_b.py" in instruction
    assert instruction.startswith("🛠️ Dispatch")


def test_issue_creation_instruction_when_none_returns_idle_message():
    instruction = issue_creation_instruction(None)
    assert "No dispatch needed" in instruction
