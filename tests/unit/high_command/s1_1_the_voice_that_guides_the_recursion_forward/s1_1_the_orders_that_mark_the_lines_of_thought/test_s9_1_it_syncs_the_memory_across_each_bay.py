"""
Filename: test_s9_1_it_syncs_the_memory_across_each_bay.py

Test for stanza memory synchronization across components.
Uses the dynamic import system from 📜 5.5 to validate memory map logic.
"""

import os
import json
import tempfile
from pathlib import Path
import pytest
import importlib.util

# ✅ Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load target module
project_root = Path(__file__).resolve().parents[5]
target_path = project_root / "src" / "storybook_fun_factory" / "high_command" / \
              "s1_1_the_orders_that_mark_the_lines_of_thought" / \
              "s9_the_hand_that_syncs_the_bays_in_verse" / "s9_1_it_syncs_the_memory_across_each_bay.py"

module = dynamic_importer.dynamic_import_module(str(target_path))
sync_stanza_memory_across_components = module.sync_stanza_memory_across_components

def test_sync_stanza_memory_across_components(tmp_path: Path):
    # Setup fake verse registries
    components = [
        "codex_builder",
        "dream_journal",
        "filename_ai",
        "memory_ai",
        "visualizer"
    ]

    for comp in components:
        path = tmp_path / "game_construction_bay" / comp / "recursion_renders" / "flowlines_of_logic"
        path.mkdir(parents=True, exist_ok=True)
        data = {
            "line1.py": {"path": f"{comp}/line1.py", "metadata": "mocked"},
            "line2.py": {"path": f"{comp}/line2.py", "metadata": "mocked"},
        }
        with open(path / "verse_registry.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

    result = sync_stanza_memory_across_components(tmp_path)

    assert isinstance(result, dict)
    assert "line1.py" in result
    for comp in components:
        assert comp in result["line1.py"]
        assert result["line1.py"][comp]["metadata"] == "mocked"
