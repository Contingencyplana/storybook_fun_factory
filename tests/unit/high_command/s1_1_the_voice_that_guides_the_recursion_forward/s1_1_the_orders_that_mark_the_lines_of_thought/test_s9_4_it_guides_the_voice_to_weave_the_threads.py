"""
Filename: test_s9_4_it_guides_the_voice_to_weave_the_threads.py

Tests the generation of High Command recursion dispatch plans.
Follows 📜 5.5-compliant dynamic import methodology.
"""

import os
import json
from pathlib import Path
import pytest
import importlib.util

# ✅ Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load target module
project_root = Path(__file__).resolve().parents[5]
target_path = project_root / "game_construction_bay" / "high_command" / \
    "s1_1_the_voice_that_guides_the_recursion_forward" / \
    "s1_1_the_orders_that_mark_the_lines_of_thought" / \
    "s9_4_it_guides_the_voice_to_weave_the_threads.py"

module = dynamic_importer.dynamic_import_module(str(target_path))
generate_dispatch_instructions = module.generate_dispatch_instructions
save_dispatch_plan = module.save_dispatch_plan

def test_generate_dispatch_instructions_and_save(tmp_path: Path):
    ready_input = {
        "line1.py": {"components": ["visualizer", "filename_ai"], "status": "ready"},
        "line2.py": {"components": ["dream_journal", "memory_ai"], "status": "ready"}
    }

    dispatch_list = generate_dispatch_instructions(ready_input)
    assert isinstance(dispatch_list, list)
    assert all("action" in d for d in dispatch_list)
    assert dispatch_list[0]["action"] == "dispatch_crossover"

    # Save to file
    output_file = tmp_path / "dispatch" / "plan.json"
    save_dispatch_plan(dispatch_list, output_file)
    assert output_file.exists()

    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[1]["target_stanza"] == "line2.py"
